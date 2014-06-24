import numpy as np
from plot import plot_trajectory
from math import cos, sin

class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0]])
        self.delta = 0.001
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor

        :The navdata contains the following values:
        :rotX - roll angle in radians (rotation around x axis)
        :rotY - pitch angle in radians (rotation around y axis)
        :rotZ - yaw angle in radians (rotation around z axis)
        :vx - velocity along the x axis
        :vy - velocity along the y axis
        '''
        
        # rotZ gives us the absolute angle around the z axis
        # positive is in the counter clockwise direction
        self.position[0] += navdata.vx*dt*cos(navdata.rotZ)
        self.position[1] += navdata.vx*dt*sin(navdata.rotZ)
        plot_trajectory("odometry", self.position)
