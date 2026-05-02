# without artifact 
async def main():
   if hub.imu.ready():
    await robot.arc(2800,20)
    # go straight and turn toward cave
    #robot straight
    # await multitask(robot.turn(20), robot.straight(300))
    # await multitask(robot.turn(-20), robot.straight(610))
    
    robot.settings(straight_speed = 400,straight_acceleration= 150, turn_rate=200, turn_acceleration=100) 
    #robot slower
   
    await robot.straight(-80.3)
    await robot.turn(70)
 
    # backup a bit

    await robot.straight(-60)
    # lower arms
    await multitask(  RAM.run_until_stalled(speed =500, duty_limit=35), #arm goes down (RAM)
     LAM.run_until_stalled(speed = 500, duty_limit=35)#arm goes down (LAM)
   )
    print(f"1 arm angle L& R : {LAM.angle()} {RAM.angle()}")
   
    wait(100)

#     # go in cave : 
   
    await robot.straight(139)

    # await LAM.run_time(-690,470)  # fork go up inside cave (LAM)
    
    # await RAM.run_time(-690,1100) # arm up (RAM)
    await multitask( RAM.run_time(-690,1100), LAM.run_time(-600,450))

    await RAM.run_time(690,990)   # right arm down 
    print(f"2 arm angle L& R : {LAM.angle()} {RAM.angle()}")
  # # backout of cave  
    await robot.straight(-125)
    await LAM.run_time(-690,800) # fork up


     # go to statue
    robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)

    await robot.turn(37) 
    await robot.straight(350)
    await RAM.run_time(-690,980) # flipper up

    # robot.settings(straight_speed = 900,straight_acceleration= 900, turn_rate=600, turn_acceleration=400)
    await robot.straight(-240)
    await robot.turn(70)
    await robot.straight(800)
    
    



# Runs the main program from start to finish.
run_task(main())