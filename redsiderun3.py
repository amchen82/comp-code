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
 
robot.settings(straight_speed = 900,straight_acceleration= 800, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)
 
async def main():
   if hub.imu.ready():
      hub.display.number(1)
      await robot.turn(88)
      await robot.straight(395)
      await RAM.run_time(1500,1100)
      await robot.straight(-120)
      await RAM.run_time(-1500,1100)
      await robot.straight(275)
      await robot.turn(-50)
      await robot.straight(200)
      await robot.turn(50)
      await robot.straight(1300)
      # robot.settings(straight_speed = 900,straight_acceleration= 700, turn_rate=600, turn_acceleration=400)
      # await robot.straight(-60)
 
      # for i in range(4):
      #    await robot.straight(88)
      #    await robot.straight(-88)
      # robot.settings(straight_speed = 900,straight_acceleration= 700, turn_rate=600, turn_acceleration=400)
      # await robot.straight(-180)
      # await robot.turn(-50)
      # await robot.straight(140)
      # await robot.turn(43)
      # await robot.straight(220)
      # await robot.turn(26)
      # await robot.straight(1000)
 
 
 
run_task(main())