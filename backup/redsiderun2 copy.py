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
    await robot.straight(-20)
    await robot.turn(-30)
    # await robot.straight(-300)
    # await robot.turn(20)
    await robot.straight(-900) #robot straight
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) #robot slower
    # await robot.straight(-100)
    # await robot.straight(100)
    await robot.turn(-90)


    # # reset  arms 
    # await RAM.run_until_stalled(speed =-180, duty_limit=35)#arm goes down (RAM)
    # RAM.reset_angle(0)

    # await wait(300)
    # await LAM.run_until_stalled(speed = -180, duty_limit=25)#arm goes down (LAM)
    # LAM.reset_angle(0)
    
    print(f"1 arm angle L& R : {LAM.angle()} {RAM.angle()}")

    # # lower arms
    # await RAM.run_target(400,380)#arm goes down (RAM)
    # await LAM.run_target(400,490) # arm go down (RAM)

    print(f"2 arm angle L& R : {LAM.angle()} {RAM.angle()}")

    wait(300)

#     # go in cave : 
    robot.settings(straight_speed = 200,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) #robot slower
    await robot.straight(60)

    # await LAM.run_target(200,500) # arm go down (RAM)
    await robot.straight(60)
    await LAM.run_target(200,515) # arm go up (RAM)
    await robot.straight(-40)
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
#     robot.settings(straight_speed = 720,straight_acceleration= 490, turn_rate=600, turn_acceleration=400)

#     await robot.turn(40) 
#     await robot.straight(328)
#     await RAM.run_target(-710,-2) # flipper up

#     robot.settings(straight_speed = 720,straight_acceleration= 600, turn_rate=600, turn_acceleration=400)
#     await robot.straight(-230)
#     await robot.turn(70)

#     await robot.straight(800)
    



# Runs the main program from start to finish.
run_task(main())