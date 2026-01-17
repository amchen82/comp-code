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
    # get brush
    # robot.straight(650)
    # robot.straight(-200)
    # robot.straight(63)
    robot.straight(613)
    # lower fork
    LAM.run_time(-5000,1200)
    LAM.run_time(5000,1000)
    # go to soils
    robot.straight(218)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=450, turn_acceleration=200)
    # get the hooked soil
    robot.turn(-45)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    # hook up
    RAM.run_time(-6000,900)

    #push soils 
    robot.straight(280)
    
    #back out 
    robot.straight(-90)
    
    #turn to return 
    robot.turn(55)
    robot.straight(-1000)
