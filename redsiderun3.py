from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction
from pybricks.tools import multitask, run_task,wait
 
hub = PrimeHub()
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.C)
LAM = Motor(Port.B)
 
wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)
 
robot.use_gyro(True)
 
robot.settings(straight_speed = 600,straight_acceleration= 800, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)
 
async def main():
   if hub.imu.ready():
      hub.display.number(1)
      robot.settings(straight_speed = 900,straight_acceleration= 500, turn_rate=600, turn_acceleration=400)
      await robot.straight(800)
      robot.settings(straight_speed = 400,straight_acceleration= 500, turn_rate=600, turn_acceleration=400)
      await LAM.run_time(400,1000)
      await robot.straight(-130)
      await robot.straight(80)
      await robot.straight(-100)
      await robot.turn(30)
      await robot.straight(-300)
      await robot.turn(-20)
      await robot.straight(500)
      await robot.turn(90)
      await RAM.run_time(3000,3000)
      await robot.straight(-150)
      await robot.turn(-30)
      #await robot.straight(150)
      #await robot.turn(30)
      #await robot.straight(1300)
 

 
run_task(main())