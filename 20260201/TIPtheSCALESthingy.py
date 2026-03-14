from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction

hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C) # lift artifact 
LAM = Motor(Port.B) # not used 

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(50)
    robot.turn(65)
    robot.straight(900)
    robot.turn(115)
    robot.straight(-150)
    robot.straight(150)
    LAM.run_time(9000,1500)
    robot.straight(170)
    robot.turn(90)
    robot.straight(-300)
    robot.turn(80)
