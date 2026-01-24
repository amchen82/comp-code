
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction

hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERC-LOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C) # lift artifact 
LAM = Motor(Port.B) # not used 

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)
# mission : rocks

if hub.imu.ready():
    robot.straight(730)
    robot.turn(25)
    robot.straight(30)
    robot.turn(-45)
    robot.turn(30)
    robot.straight(-50)
    robot.turn(32)

    # get the hook artifact
    robot.straight(15)
    # lower arm
    RAM.run_time(-600,1200)
    robot.settings(straight_speed = 350,straight_acceleration= 80, turn_rate=600, turn_acceleration=400)
    robot.straight(55)
    #lift arm with artifact
    RAM.run_time(1000,1000)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    #back out 
    robot.straight(-25)
    robot.turn(-60)
    robot.straight(-75)
    robot.turn(100)
    robot.settings(straight_speed = 720,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
    robot.straight(500)
    robot.turn(80)
    robot.straight(1000)
   