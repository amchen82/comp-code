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

robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=800, turn_acceleration=700)
hub.imu.reset_heading(0)

if hub.imu.ready():
    # # robot.straight(600)
    # # robot.turn(-50)
    # # robot.straight(300)
    robot.arc(-1030,51)
    RAM.run_time(-700,700)
    robot.straight(-118)
    robot.turn(-42)
    robot.straight(750)
    robot.turn(-60)
    robot.straight(150)
    RAM.run_time(900,1200)
    LAM.run_time(700,1000)
    robot.straight(-125)
    robot.turn(58)
    robot.straight(230)
    robot.turn(-90)
    # robot.straight(30)
    # robot.straight(150)
    # robot.straight(-105)
    # robot.turn(100)
    # robot.straight(120)
    # # robot.arc(-1050,44)
    # # robot.turn(-70)
    # # robot.straight(100)
    # # LAM.run_time(1000,1100)
    # # robot.straight(-120)
    # # robot.turn(-78)
    # # robot.straight(-220)
    # #robot.turn(-76)
    # #robot.arc(230,83)