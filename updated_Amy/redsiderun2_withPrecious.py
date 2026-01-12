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
 
robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
    await robot.straight(-1000) #robot straight
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) #robot slower
    await robot.straight(25)
    await robot.turn(-90)
    # await multitask(RAM.run_time(690,1060),LAM.run_until_stalled(300, duty_limit=40)) #arm goes down (LAM+RAM)
    await multitask(RAM.run_time(690,1060),LAM.run_time(690, 1069))
   
    print("flipper up, fork  up")
    print(f"step 1 : right arm angle : {RAM.angle()}")
    print(f"step 1 : left arm angle : {LAM.angle()}")
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100)
    await robot.straight(62)
    wait(100)
  # inside cave 
   
    await multitask(RAM.run_time(0,0),LAM.run_time(690,380)) #arm goes down (LAM+RAM)
    print(" fork slightly dn")
    print(f"step 2 : right arm angle : {RAM.angle()}")
    print(f"step 2 : left arm angle : {LAM.angle()}")

    robot.settings(straight_speed = 190,straight_acceleration= 50, turn_rate=100, turn_acceleration=70)
    await robot.straight(47)
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100)
 
    await multitask(RAM.run_time(-690,1110),LAM.run_time(-690,380))  # arm go up (LAM)
    print("flipper up, fork slightly up")
    print(f"step 3 : right arm angle : {RAM.angle()}")
    print(f"step 3 : left arm angle : {LAM.angle()}")
    await multitask(RAM.run_time(690,1010),LAM.run_time(0,0)) #arm goes dn (RAM)
    print("flipper down")
    print(f"step 4 : right arm angle : {RAM.angle()}")  
    print(f"step 4 : left arm angle : {LAM.angle()}")
    await wait(930)
    await robot.straight(-30)
    # await robot.turn(5.3)
    await robot.straight(-90)
    # await RAM.run_target(-690,-2) # flipper up
    LAM.run_time(-550,626)
    robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)

    await robot.turn(40) 
    await robot.straight(328)
    await RAM.run_target(-699,-2) # flipper up
    await robot.straight(-330)
    await robot.turn(70)

    # await robot.turn(110)
    await multitask(RAM.run_time(0,0),LAM.run_time(-150,626))
    await robot.straight(800)
    



# Runs the main program from start to finish.
run_task(main())