from plot import plot

class UserCode:
    def __init__(self):
        # initialize data you want to store in this object between calls to the measurement_callback() method
        self.last_yaw = 0
        self.max_roll = 0
        self.max_pitch = 0
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''
        # add your plot commands here
        plot("roll", navdata.rotX);
        self.max_roll = max(self.max_roll, navdata.rotX)
        self.max_pitch = max(self.max_pitch, navdata.rotY)
        self.max_yaw = max(self.max_yaw, navdata.rotZ)
        print "max_roll:", self.max_roll
