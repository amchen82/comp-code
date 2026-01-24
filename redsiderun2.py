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
    # go straight and turn toward cave
    await robot.straight(90)
    await robot.turn(20)
    await robot.straight(300)
    await robot.turn(-20)
    await robot.straight(610) #robot straight
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) #robot slower
   
    await robot.straight(-100)
    await robot.turn(90)


    # reset  arms 
    await RAM.run_until_stalled(speed =180, duty_limit=35)#arm goes down (RAM)
    RAM.reset_angle(0)

  
    
    print(f"1 arm angle L& R : {LAM.angle()} {RAM.angle()}")

    # lower arms
    # await RAM.run_target(400,200)#arm goes down (RAM)
    # await LAM.run_target(400,780) # arm go down (RAM)
    await LAM.run_until_stalled(speed = 180, duty_limit=35)#arm goes down (LAM)
    LAM.reset_angle(0)
    print(f"2 arm angle L& R : {LAM.angle()} {RAM.angle()}")

    wait(300)

#     # go in cave : 
    # robot.settings(straight_speed = 100,straight_acceleration= 40, turn_rate=200, turn_acceleration=100) #robot slower
    await robot.straight(110)

    # await LAM.run_target(200,500) # arm go down (RAM)
    # await robot.straight(60)
    # await LAM.run_target(200,400) # arm go up (RAM)
    await LAM.run_time(-690,470)  # arm go up (LAM)
    
    await RAM.run_time(-690,930) # arm down (RAM)
    await RAM.run_time(690,800)   # right arm down a bit
    print(f"2 arm angle L& R : {LAM.angle()} {RAM.angle()}")
    # await RAM.run_target(-200, 600)  # right arm up a bit
    print(f"2 arm angle L& R : {LAM.angle()} {RAM.angle()}")
    # await RAM.run_target(400, 100)   # right arm down a bit
    await robot.straight(-125)
    await LAM.run_time(-690,620) # fork up
#     # raise left arm(fork) a little 
#     await LAM.run_target(-100, -600)
#     # raise right arm up and dn
#     await RAM.run_target(-100, 100)  
#     await RAM.run_target(400, 400)
#     print(f"3 right arm angle : {RAM.angle()}")

# # backout of cave
#     await robot.straight(-120)
#     LAM.run_target(-400,20) # fork up 
 
#     # go to statue
    robot.settings(straight_speed = 720,straight_acceleration= 490, turn_rate=600, turn_acceleration=400)

    await robot.turn(40) 
    await robot.straight(328)
    await RAM.run_time(-690,980) # flipper up

    robot.settings(straight_speed = 720,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
    await robot.straight(-230)
    await robot.turn(70)

    await robot.straight(800)
    



# Runs the main program from start to finish.
run_task(main())