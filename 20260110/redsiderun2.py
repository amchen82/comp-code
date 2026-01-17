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
    await robot.straight(-980) #robot straight
    # robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) #robot slower
    await robot.straight(25)
    await robot.turn(-90)
    await RAM.run_time(690,1700)#arm goes down (RAM)

   
    print("flipper dn")
    print(f"step 1 : right arm angle : {RAM.angle()}")
  
    robot.settings(straight_speed = 220,straight_acceleration= 300, turn_rate=200, turn_acceleration=100)
    await robot.straight(95)
    await robot.turn(-8)
    wait(100)

 
    await RAM.run_time(-690,970)  # arm go up (LAM)
    print("flipper up")
    print(f"step 3 : right arm angle : {RAM.angle()}")

    await RAM.run_time(690,830) #arm goes dn (RAM)
    print("flipper down")
    print(f"step 4 : right arm angle : {RAM.angle()}")  
 
    await wait(230)
    await robot.straight(-120)
    
    robot.settings(straight_speed = 720,straight_acceleration= 490, turn_rate=600, turn_acceleration=400)

    await robot.turn(40) 
    await robot.straight(328)
    await RAM.run_target(-710,-2) # flipper up

    robot.settings(straight_speed = 720,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
    await robot.straight(-230)
    await robot.turn(70)

    await robot.straight(800)
    



# Runs the main program from start to finish.
run_task(main())