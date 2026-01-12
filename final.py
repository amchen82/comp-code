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

robot.settings(straight_speed = 520,straight_acceleration= 300, turn_rate=600, turn_acceleration=200)
hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(650)
    robot.turn(29)
    robot.straight(500)
    robot.straight(-200)
    robot.turn(-15)
    robot.straight(-800) 
   