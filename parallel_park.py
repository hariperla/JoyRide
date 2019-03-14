# Before running any code changes make sure to click the button "Restart Connection" above first.
# Also make sure to click Reset in the simulator to refresh the connection.
# After making any code changes, make sure to click the button "Restart Connection" above first. Then re-run your code cell (Ctrl+Enter).
# You need to wait for the Kernel Ready message.

car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    
    # TODO: Use WASD keys in simulator to gain an intuitive feel of parallel parking.
    # Pay close attention to the time, position, and velocity in the simulator.
    
    # TODO: Use this information to make decisions about how to set your car parameters
    
    # In this code below the car will drive reverse for 8.5 and steer 4% of 25deg left
    # and then move forward with a steering angle to 87% of 25deg right until time is less than 11.8 seconds
    # and then car will move forward and turn left with a steering angle of 78% of 25deg until
    # pos_y is less than 33.4 and time is less than 15.0 seconds. The car will then readjust it's 
    # position in the lane until 15.8 seconds and pos_y is greater than 30.5 and then comes to a stop by braking
       
    if time < 8.5:
        car_parameters['throttle'] = -1
        car_parameters['steer'] = -0.04
    elif time < 11.8:
        car_parameters['throttle'] = 1.0
        car_parameters['steer'] = 0.87
    elif pos_y < 33.4 and time < 15.0 :
        car_parameters['throttle'] = 1
        car_parameters['steer'] = -0.78
    elif time < 15.8 and pos_y > 30.5:
        car_parameters['throttle'] = -1
        car_parameters['steer'] = 0.7
    else:
        car_parameters['throttle'] = 0
        car_parameters['brake'] = 1
        
    return car_parameters
    
import src.simulate as sim
sim.run(control)
