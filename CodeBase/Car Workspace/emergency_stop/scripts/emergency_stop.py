import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import Empty

class EmergencyStop:

     def __init__(self):
	    #TODO: initiate AckermannDriveStamped message that will be published
        self.ack_msg = AckermannDriveStamped()
        self.ack_msg.header.stamp = rospy.Time.now()
        self.ack_msg.header.frame_id = ''
        self.ack_msg.drive.steering_angle = 0 
        self.ack_msg.drive.speed = 0

        self.ems = False

        self.pub = rospy.Publisher("/vesc/high_level/ackermann_cmd_mux/input/nav_0", AckermannDriveStamped, queue_size=10)
        
        self.sub = rospy.Subscriber("/ems_relase", Empty, self.callback)

    def check_connection(self):
        #if screen not connected
        result = subprocess.call(['./brake_check.sh'], shell=True)
        print(result)
        if(result == 1)
            self.pub.publish(self.ack_msg)
            self.ems = True

    def callback(self):
        self.ems = False


if __name__=='__main__':
    rospy.init_node("emergency_stop_node")
    ems = EmergencyStop()
    rospy.loginfo("Initialized: emergency_stop_node")
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        ems.check_connection()
        rate.sleep()