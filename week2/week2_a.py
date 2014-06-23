from plot import plot

class UserCode:
    def __init__(self):
        # initialize data you want to store in this object between calls to the measurement_callback() method
        self.last_yaw = 0
        self.max_roll = 0
        self.max_pitch = 0
        self.max_yaw = 0
        self.theta_x = 0
        self.theta_y = 0
        self.theta_z = 0
        
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
        # add your plot commands here
        # plot("roll", navdata.rotX)
        # plot("pitch", navdata.rotY)
        # plot("yaw", navdata.rotZ)
        # self.max_roll = max(self.max_roll, abs(navdata.rotX))
        # self.max_pitch = max(self.max_pitch, abs(navdata.rotY))
        # self.max_yaw = max(self.max_yaw, abs(navdata.rotZ))
        self.theta_x += navdata.rotX
        self.theta_z += navdata.rotZ
        plot("rot z", navdata.rotZ)
        # plot("theta z", self.theta_z)
    
    def __del__(self):
        print "max_roll:", self.max_roll
        print "max_pitch:", self.max_pitch
        print "max_yaw:", self.max_yaw
