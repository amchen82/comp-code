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
    robot.straight(680) # faster???
    # Mission 2
  
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=450, turn_acceleration=200)
    robot.turn(-45)
    robot.settings(straight_speed = 900,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
    ## Grab one of the top soil missons
    robot.straight(153)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=450, turn_acceleration=200)
    RAM.run_time(-6000,900)
    #option 2 : using square with rubber band
    # robot.straight(-100)
    # LAM.run_time(-6000,900)

    robot.straight(-135)
    robot.turn(40)
    robot.settings(straight_speed = 950,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
    robot.straight(-87)
    LAM.run_time(-4700,1200)
    LAM.run_time(5000,1000)
    robot.settings(straight_speed = 950,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)
    
    robot.turn(20)
    robot.straight(-800)
