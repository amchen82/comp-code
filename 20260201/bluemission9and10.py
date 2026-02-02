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
#mission : ring and table

if hub.imu.ready():
    robot.straight(75)
    robot.turn(-43)
    robot.straight(450)
    LAM.run_time(800,590) #LAM - inside the ring
    LAM.run_time(-200,400) #LAM - secures the ring
    RAM.run_time(2200,1000) #RAM goes down
    wait(700)
    LAM.run_time(-100,1800) #pulls back the ring
    robot.straight(-160)
    wait(550)
    robot.straight(20)
    RAM.run_time(-800,150) #arm goes up slighty 
    wait(550)
    robot.straight(20)
    RAM.run_time(-600,1000) #RAM goes up all the way
    robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)
    robot.straight(-700)
    
    