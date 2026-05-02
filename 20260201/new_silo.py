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

robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)

hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(100)
    robot.turn(-45)
    robot.straight(65)
    robot.turn(45)
    robot.straight(628)
    robot.turn(-31)
    print(hub.imu.heading())
    robot.straight(-40)
    robot.turn(78)
    print(hub.imu.heading())
    robot.turn(-8)
    robot.straight(10)
    robot.turn(6)
    robot.straight(-40)
    # # turn back  
    RAM.run_time(-680,1080)# arm down 
    robot.straight(30)
    robot.settings(straight_speed = 350,straight_acceleration= 80, turn_rate=600, turn_acceleration=400)
    robot.straight(55) 
    RAM.run_time(700,1000)# arm up
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    robot.straight(-82)
    robot.turn(-130)
    robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=900, turn_acceleration=900)
    robot.straight(-290)
    robot.straight(35) # drive less
    for i in range(4):
         LAM.run_time(-9900, 900)
         LAM.run_time(9900, 900)
    robot.arc(-280,180)