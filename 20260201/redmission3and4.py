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
    
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) 
    #robot slower
   
    await robot.straight(-90)
    await robot.turn(90)
    # backup a bit
    robot.settings(straight_speed = 220,straight_acceleration= 100, turn_rate=200, turn_acceleration=100) 
    await robot.straight(-25)
    # lower arms
    await multitask(  RAM.run_until_stalled(speed =360, duty_limit=35), #arm goes down (RAM)
     LAM.run_until_stalled(speed = 360, duty_limit=35)#arm goes down (LAM)
   )
    print(f"1 arm angle L& R : {LAM.angle()} {RAM.angle()}")
   
    wait(300)

#     # go in cave : 
   
    
    await robot.straight(135)

    await LAM.run_time(-690,470)  # fork go up inside cave (LAM)
    
    await RAM.run_time(-690,1100) # arm up (RAM)
    await RAM.run_time(690,990)   # right arm down 
    print(f"2 arm angle L& R : {LAM.angle()} {RAM.angle()}")
    
    await robot.straight(-125)
    await LAM.run_time(-690,800) # fork up


# # backout of cave

 
     # go to statue
    robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)

    await robot.turn(40) 
    await robot.straight(328)
    await RAM.run_time(-690,980) # flipper up

    # robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)
    await robot.straight(-230)
    await robot.turn(70)

    await robot.straight(800)
    



# Runs the main program from start to finish.
run_task(main())