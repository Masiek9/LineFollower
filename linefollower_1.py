
# from controller import Camera
from controller import Robot

def run_robot(robot):

    time_step = 32
    max_speed = 6.28
    
    #motors
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # Step simulation
    while robot.step(time_step) != -1:
        left_speed = max_speed
        right_speed = max_speed
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    
    
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
    
    
    


