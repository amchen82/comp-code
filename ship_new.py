from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction
from pybricks.tools import multitask, run_task,wait
 
hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C)
LAM = Motor(Port.B)#fork 
 
wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)
 
robot.use_gyro(True)
 
robot.settings(straight_speed = 720,straight_acceleration= 500, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)
# without artifact 
async def main():
   if hub.imu.ready():
    # go straight towards ship
    await robot.straight(100) #robot straight
   
    # reset  arms 
    await RAM.run_until_stalled(speed = -180, duty_limit=40)
    
    RAM.reset_angle(0)

    #arm goes down 
    await RAM.run_target(200,400)

    for i in range(10):
      await robot.straight(-10)
      await robot.straight(10)

   await RAM.run_target(-200,0)
   await robot.straight(100)




run_task(main())