#!/usr/bin/env python
import sys
import math
import numpy as np

# ROS Imports
import rospy
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped

class WallFollow:
    """ Implement Wall Following on the car
    """
    def __init__(self):
        #Topics & Subs, Pubs
        lidarscan_topic = '/scan'
        drive_topic = '/drive'

        self.lidar_sub = rospy.Subscriber(lidarscan_topic, LaserScan, self.lidar_callback) #TODO: Subscribe to LIDAR
        self.drive_pub = rospy.Publisher(drive_topic, AckermannDriveStamped, queue_size=10) #TODO: Publish to drive

        # Parameters
        self.D = 1.0 # default D
        self.window_size = 5 # to compute a, b as mean values
        self.theta = math.radians(40) # theta, your choice
        self.theta_comp = math.pi/2 - self.theta # the complement angle of theta

        # PID CONTROL PARAMS
        self.kp = 1.3
        self.ki = 0
        self.kd = -0.01
        self.prev_error = 0
        self.error = 0
        self.integral = 0

        self.min_angle = -0.4
        self.max_angle = 0.4
        self.servo_offset = 0 # offset of the car
        self.angle = 0 # initial steering angle
        self.velocity = 1 # initial velocity
        self.freq = 10.0 # control frequency

        ## Driving msg
        self.drive_msg = AckermannDriveStamped()
        self.drive_msg.header.stamp = rospy.Time.now()
        self.drive_msg.header.frame_id = "laser"
        self.drive_msg.drive.steering_angle = self.angle
        self.drive_msg.drive.speed = 1

    def rawDistances(self, data):
        # TODO: Calculate disance of the car to both sides
        # data is from the LiDAR, of type LaserScan
        idx_middle = int(len(data.ranges)/2) # TODO: calculate the index of the data point right in the middle (right in front of the car)
        inc = data.angle_increment
        # Calculate indices of the rays to measure the distances a and b for both sides
        idx_b_r = idx_middle - int(math.radians(90)/inc)
        idx_a_r = idx_middle - int(self.theta_comp/inc)
        idx_b_l = idx_middle + int(math.radians(90)/inc)
        idx_a_l = idx_middle + int(self.theta_comp/inc)

        a_l = np.nanmean(data.ranges[idx_a_l-self.window_size : idx_a_l+self.window_size])
        b_l = np.nanmean(data.ranges[idx_b_l-self.window_size : idx_b_l+self.window_size])
        a_r = np.nanmean(data.ranges[idx_a_r-self.window_size : idx_a_r+self.window_size])
        b_r = np.nanmean(data.ranges[idx_b_r-self.window_size : idx_b_r+self.window_size])
        return a_l, b_l, a_r, b_r


    def distanceSide(self, a, b):
        #TODO: Calculate distance of the car to one side, given a and b distances and the angle theta
        alpha = math.atan2((a*math.cos(self.theta)-b),a*math.sin(self.theta))
        D_t = b*math.cos(alpha)
        D_t_1 = D_t + (self.velocity*(1/self.freq))*math.sin(alpha)
        return D_t_1


    def selectVel(self, angle):
        # TODO: Select velocity from discrete incremental rules
        angle_abs = abs(angle)
        if angle_abs > math.radians(20):
            velocity = .3
        elif angle_abs > math.radians(10):
            velocity = 0.5
        else:
            velocity = 0.7
        return velocity

    def limitAngle(self, angle):
        # TODO: Limit / Saturate the steering angle to the range [min_angle, max_angle]
        angle = angle + self.servo_offset
        if angle > self.max_angle:
            angle = self.max_angle
        elif angle < self.min_angle:
            angle = self.min_angle
        return angle

    def pid_control(self, error, prev_error):
        self.integral = self.integral + error * (1/self.freq) # TODO: update integral term
        derivative = (error - prev_error)/(1/self.freq)
        angle = (self.kp * error) + (self.kd * derivative) + (self.ki * self.integral) # TODO: PID control equation to calculate the angle control command
        #TODO: Calculate velocity from angle follow discrete increment rules provided in the document
        velocity = self.selectVel(angle) # calculate velocity from angle
        return angle, velocity


    def lidar_callback(self, data):
        # TODO: Estimate raw distances to both sides (a_l, b_l, a_r, b_r)
        # from laser scanned message (i.e., data)
        a_l, b_l, a_r, b_r = self.rawDistances(data)

        # TODO: Calculate distance to the left side (D_t+1 for left side)
        D_l = self.distanceSide(a_l, b_l)
        D_r = self.distanceSide(a_r, b_r)
        self.D = (D_l + D_r)/2.0 
        
        # TODO: Calculate prev_error and error
        # prev_error store the previous error
        # error is the current error, error = D - D_t+1
        self.prev_error = self.error
        self.error = D_l - self.D

        #TODO: Compute steering angle and velocity usiing current error and previous error
        self.angle, self.velocity = self.pid_control(self.error, self.prev_error)

        ## TODO: Update driving message
        self.drive_msg.header.stamp = rospy.Time.now()
        self.drive_msg.drive.steering_angle = self.limitAngle(self.angle) # using limitAngle to limit the angle in the range [min_angle, max_angle]
        self.drive_msg.drive.speed = self.velocity
        if(self.drive_msg.drive.steering_angle < 0):
            rospy.loginfo("steer %.3f - speed %1.3f", self.drive_msg.drive.steering_angle, self.drive_msg.drive.speed)


def main(args):
    rospy.init_node("WallFollow_node", anonymous=True)
    wf = WallFollow()
    rate = rospy.Rate(wf.freq)
    while not rospy.is_shutdown():
        wf.drive_pub.publish(wf.drive_msg)
        rate.sleep()

if __name__=='__main__':
	main(sys.argv)