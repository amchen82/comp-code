
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

robot.settings(straight_speed = 820,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)
# mission : rocks

if hub.imu.ready():
    robot.straight(634)
   # robot.settings(straight_speed = 820,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
   # robot.straight(200)
    robot.straight(-40)
    LAM.run_time(-700,3000)
    RAM.run_time(-700,3700)
    LAM.run_time(1000,1200)
    robot.straight(-700)
   