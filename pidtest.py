from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, multitask, run_task, StopWatch
from umath import pi

# =========================
# Hardware setup
# =========================
hub = PrimeHub()

leftWheel  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightWheel = Motor(Port.E, Direction.CLOCKWISE)

LAM = Motor(Port.C, Direction.COUNTERCLOCKWISE)
RAM = Motor(Port.B, Direction.COUNTERCLOCKWISE)

# =========================
# Robot geometry
# =========================
WHEEL_DIAMETER_MM = 62.4
AXLE_TRACK_MM     = 110.0

WHEEL_CIRC_MM = pi * WHEEL_DIAMETER_MM
MM_PER_DEG = WHEEL_CIRC_MM / 360.0
DEG_PER_MM = 360.0 / WHEEL_CIRC_MM

# =========================
# Editable defaults (change anytime in main)
# Units:
#  - straight_speed: mm/s
#  - straight_acceleration: mm/s^2
#  - turn_rate: deg/s
#  - turn_acceleration: deg/s^2
# =========================
DRIVE_DEFAULTS = {
    "straight_speed": 450,
    "straight_acceleration": 900,
    "turn_rate": 260,
    "turn_acceleration": 900,
}

def set_drive_defaults(*, straight_speed=None, straight_acceleration=None,
                       turn_rate=None, turn_acceleration=None):
    """Optional helper to update defaults cleanly."""
    if straight_speed is not None:
        DRIVE_DEFAULTS["straight_speed"] = straight_speed
    if straight_acceleration is not None:
        DRIVE_DEFAULTS["straight_acceleration"] = straight_acceleration
    if turn_rate is not None:
        DRIVE_DEFAULTS["turn_rate"] = turn_rate
    if turn_acceleration is not None:
        DRIVE_DEFAULTS["turn_acceleration"] = turn_acceleration


# =========================
# Utilities
# =========================
def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x

def avg_distance_mm(start_l_deg, start_r_deg):
    dl = (leftWheel.angle()  - start_l_deg) * MM_PER_DEG
    dr = (rightWheel.angle() - start_r_deg) * MM_PER_DEG
    return (dl + dr) / 2.0

def set_chassis_speeds(v_mm_s, w_deg_s):
    """
    Differential drive kinematics.
    +w is CLOCKWISE to match hub.imu.heading() convention.
    """
    w_rad_s = (w_deg_s * pi) / 180.0
    half = AXLE_TRACK_MM / 2.0

    v_left  = v_mm_s + (w_rad_s * half)
    v_right = v_mm_s - (w_rad_s * half)

    leftWheel.run(v_left * DEG_PER_MM)
    rightWheel.run(v_right * DEG_PER_MM)

async def brake_stop():
    leftWheel.brake()
    rightWheel.brake()
    await wait(50)


# =========================
# PID controller
# =========================
class PID:
    def __init__(self, kp, ki, kd, integral_limit=None, output_limit=None):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral_limit = integral_limit
        self.output_limit = output_limit
        self.reset()

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0
        self.initialized = False

    def update(self, error, dt):
        if not self.initialized:
            self.prev_error = error
            self.initialized = True

        self.integral += error * dt
        if self.integral_limit is not None:
            self.integral = clamp(self.integral, -self.integral_limit, self.integral_limit)

        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        self.prev_error = error

        out = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        if self.output_limit is not None:
            out = clamp(out, -self.output_limit, self.output_limit)

        return out


# =========================
# Motion: centimeters + degrees
# =========================
async def move_cm(cm,
                  straight_speed=None,
                  straight_acceleration=None,
                  dist_tol_mm=3.0,
                  settle_ms=120,
                  timeout_ms=6000):
    """
    Drive straight for 'cm' centimeters with PID distance + PID heading hold (gyro).

    Optional:
      - straight_speed (mm/s)
      - straight_acceleration (mm/s^2)
    """
    if straight_speed is None:
        straight_speed = DRIVE_DEFAULTS["straight_speed"]
    if straight_acceleration is None:
        straight_acceleration = DRIVE_DEFAULTS["straight_acceleration"]

    target_mm = cm * 10.0

    start_l = leftWheel.angle()
    start_r = rightWheel.angle()
    heading0 = hub.imu.heading()

    dist_pid = PID(kp=4.0, ki=0.02, kd=0.55,
                   integral_limit=8000,
                   output_limit=straight_speed)

    head_pid = PID(kp=9.0, ki=0.00, kd=0.70,
                   integral_limit=200,
                   output_limit=260)  # max turn correction while driving

    sw = StopWatch()
    last_t = sw.time()
    v_cmd = 0.0
    settled = 0

    while True:
        now = sw.time()
        dt = (now - last_t) / 1000.0
        if dt <= 0:
            dt = 0.02
        last_t = now

        traveled = avg_distance_mm(start_l, start_r)
        err_mm = target_mm - traveled

        v_des = dist_pid.update(err_mm, dt)

        # Slew-rate limit for smoothness
        dv = straight_acceleration * dt
        v_cmd += clamp(v_des - v_cmd, -dv, dv)

        # Hold heading (gyro correction)
        heading_err = heading0 - hub.imu.heading()
        w_cmd = head_pid.update(heading_err, dt)

        set_chassis_speeds(v_cmd, w_cmd)

        # settle
        if abs(err_mm) <= dist_tol_mm and abs(v_cmd) < 60:
            settled += int(dt * 1000)
            if settled >= settle_ms:
                break
        else:
            settled = 0

        if now >= timeout_ms:
            break

        await wait(20)

    await brake_stop()


async def turn_deg(deg,
                   turn_rate=None,
                   turn_acceleration=None,
                   ang_tol_deg=1.0,
                   settle_ms=120,
                   timeout_ms=5000):
    """
    Turn in place by 'deg' degrees using gyro-based PID.
    Positive degrees = clockwise.

    Optional:
      - turn_rate (deg/s)
      - turn_acceleration (deg/s^2)
    """
    if turn_rate is None:
        turn_rate = DRIVE_DEFAULTS["turn_rate"]
    if turn_acceleration is None:
        turn_acceleration = DRIVE_DEFAULTS["turn_acceleration"]

    start_heading = hub.imu.heading()
    target_heading = start_heading + deg

    turn_pid = PID(kp=7.5, ki=0.03, kd=0.85,
                   integral_limit=500,
                   output_limit=turn_rate)

    sw = StopWatch()
    last_t = sw.time()
    w_cmd = 0.0
    settled = 0

    while True:
        now = sw.time()
        dt = (now - last_t) / 1000.0
        if dt <= 0:
            dt = 0.02
        last_t = now

        err = target_heading - hub.imu.heading()
        w_des = turn_pid.update(err, dt)

        # Slew-rate limit
        dw = turn_acceleration * dt
        w_cmd += clamp(w_des - w_cmd, -dw, dw)

        set_chassis_speeds(0.0, w_cmd)

        if abs(err) <= ang_tol_deg and abs(w_cmd) < 40:
            settled += int(dt * 1000)
            if settled >= settle_ms:
                break
        else:
            settled = 0

        if now >= timeout_ms:
            break

        await wait(20)

    await brake_stop()


# =========================
# Main example
# =========================
async def main():
    while not hub.imu.ready():
        await wait(10)
    
    print(hub.battery.voltage())

    hub.imu.reset_heading(0)
    await wait(200)
    print("start")

    # Change defaults in the middle of main (affects future moves/turns)
    DRIVE_DEFAULTS["straight_speed"] = 300
    DRIVE_DEFAULTS["straight_acceleration"] = 700

    # Uses defaults (because args omitted)
    await move_cm(20)

    # Override defaults for this one call (Option A style)
    await move_cm(20, straight_speed=200, straight_acceleration=500)

    await multitask(
        RAM.run_time(200, 2000),
        LAM.run_time(200, 2000)
    )

    # Faster travel just for this call
    await move_cm(60, straight_speed=600, straight_acceleration=1400)

    # Slow turn (more accurate)
    await turn_deg(90, turn_rate=120, turn_acceleration=400)

    # Change default turn settings mid-main
    set_drive_defaults(turn_rate=220, turn_acceleration=700)

    # Uses new default turn settings (args omitted)
    await turn_deg(-1000)


run_task(main())