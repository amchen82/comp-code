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
    # Mission 1 
    ## Soil Deposits
    # robot.straight(650)
    # robot.straight(-200)
    # robot.straight(63)
    # ## Brush Pickup
    # LAM.run_time(-5000,1200)
    # LAM.run_time(5000,1000)
    robot.straight(687)
    # Mission 2
  
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=450, turn_acceleration=200)
    robot.turn(-44)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
    ## Grab one of the top soil missons
    robot.straight(153)
    RAM.run_time(-6000,900)
    robot.straight(-170)
    robot.turn(73)
    robot.straight(-800)
#     robot.straight(-90)
#     robot.turn(55)

#     # Back to start
#     robot.straight(-1000)


#     # robot.straight(-20)
#     # robot.turn(-22) # push the red rod
#     # robot.settings(straight_speed = 720,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
#     # robot.turn(100)
#     # robot.straight(-1000)
   
#   # robot.straight(218)
#     # robot.straight(650)


#     # robot.straight(-20)
#     # robot.straight(-200)
#     # robot.turn(100)
#     # robot.straight(-800)