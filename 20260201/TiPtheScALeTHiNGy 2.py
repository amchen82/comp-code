from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction
from pybricks.tools import wait

hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C)
LAM = Motor(Port.B)

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

if hub.imu.ready():
    # robot.straight(600)
    # robot.turn(-50)
    # robot.straight(300)
    robot.arc(-1195,45)
    RAM.run_time(-700,700)
    robot.straight(-65)
    robot.turn(-67)
    robot.arc(230,80)
    # robot.straight(80)
    # robot.settings(straight_speed = 220,straight_acceleration= 200, turn_rate=150, turn_acceleration=150)
    # robot.turn(53)
    # robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    # robot.straight(160) 
    robot.straight(-175)
    robot.turn(-68)
    robot.straight(600)
    robot.turn(-90)
    RAM.run_time(1300,1200)
    RAM.run_time(-1300,1200)
    robot.straight(150)
    LAM.run_time(700,1000)
    robot.straight(-115)
    robot.turn(87)
    robot.straight(230)
    robot.turn(-180)
    robot.straight(-40)
    robot.turn(-90)