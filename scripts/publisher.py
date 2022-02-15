#!/usr/bin/env python

# a publisher node

"""
rostopic pub /mobile_base_controller/cmd_vel geometry_msgs/Twist -r 3 -- '[0.0,0.0,0.0]' '[0.0, 0.0, 0.3]'
"""

from cmath import pi
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
import subprocess
import os
import sys

def call_localization_service():
    print("CALLING /global_localization SERVICE .......")
    # home = os.environ['HOME']
    # current_directory = os.getcwd()
    # path to the directory of current python file
    dir_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filepath = dir_path + "/call_localization_service.sh"
    print(filepath)
    subprocess.call(filepath)
    print("END.........")


def call_clear_costmaps_service():
    print("CALLING /move_base/clear_costmaps SERVICE .......")
    dir_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filepath = dir_path +  "/call_clear_costmaps_service.sh"
    subprocess.call(filepath)
    print("END.........")



def rotate():
    # Publisher(topic, message type, queue_size limits amt of queued messages)
    pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=10)

    # (node name, ensures node is unique)
    rospy.init_node('rotate', anonymous=True)


    # publish 3 messages/second to keep constant velocity
    rate = rospy.Rate(3) # 3hz

    # simulation time is slower than real time; we are using real time here (by using python's time.time())
    real_time_factor = 0.5

     # define variables
    angular_v = 0.5
    num_rotation = 1
    end_time = 2 * pi * num_rotation/angular_v/real_time_factor
    elapsed_time = 0

    # record start time
    start_time = time.time()
    
    # while elapsed < end:
    while elapsed_time < end_time:
        # the message to publish to topic
        msg = Twist()
        msg.angular.z = 0.3
        
        # log
        rospy.loginfo(msg)
        
        # publish
        pub.publish(msg)

        # sleep the right amt of time so that rate is 3hz
        rate.sleep()

        # get time elasped
        elapsed_time = time.time() - start_time

        print("ELAPSED TIME", elapsed_time)
        print("END", end_time)
        
    

       

if __name__ == '__main__':
    try:
        call_localization_service()
        time.sleep(2)
        rotate()
        time.sleep(1)
        call_clear_costmaps_service()
        rotate()
        print("LOCALIZATION SUCCESSFUL")
    except rospy.ROSInterruptException:
        pass
