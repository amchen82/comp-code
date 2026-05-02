from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction,Stop
from pybricks.tools import multitask, run_task,wait

hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C) # lift artifact 
LAM = Motor(Port.B) # not used 

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 900,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(25)
    robot.turn(65)
    robot.straight(985)
    robot.turn(115)
    robot.straight(-150)
    robot.straight(150)
    LAM.run_time(9000,1100)
    robot.straight(170)
    robot.turn(90)
    robot.straight(-450)
    robot.turn(50)
    robot.straight(130)
    RAM.run_time(850,1100)
    robot.straight(-145)
    robot.straight(30)
    RAM.run_time(-850,1100)
    robot.straight(110)
    robot.settings(straight_speed = 900,straight_acceleration= 600, turn_rate=600, turn_acceleration=300)
    robot.turn(-88,Stop.NONE)
    # robot.straight(10,Stop.NONE)
    robot.turn(88,Stop.NONE)
    robot.straight(-1000)





    # robot.turn(48)
    # robot.straight(30)
    # RAM.run_time(850,1100) 
    # robot.straight(20)
    # robot.settings(straight_speed = 670,straight_acceleration= 400, turn_rate=600, turn_acceleration=400)
    # robot.straight(-300)
    # robot.turn(15)
    # robot.straight(80)
    # robot.turn(-40) 
    # robot.straight(-500)

    # # multitask(robot.straight(-200), RAM.run_time(-2000,1400)) #dnt fix


