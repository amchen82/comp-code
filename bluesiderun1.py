
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
    robot.straight(534)
    # # # silo
    LAM.run_time(500,500)
    LAM.run_time(-500,500)
    LAM.run_time(1000,600)
    LAM.run_time(-500,600)
    LAM.run_time(600,600)
    LAM.run_time(-500,600)
    LAM.run_time(9000,1000)
    # #travel to next location
    robot.straight(231)

    robot.turn(-31)
    robot.straight(-9)
    robot.turn(81)
    robot.straight(15)
    
    RAM.run_time(-600,1000)
    robot.settings(straight_speed = 350,straight_acceleration= 80, turn_rate=600, turn_acceleration=400)
    robot.straight(55)
    RAM.run_time(700,1000)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    robot.straight(-120)
    robot.turn(-132)
    robot.straight(-400)
    