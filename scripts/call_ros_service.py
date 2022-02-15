#!/usr/bin/env python

import rospy
from global_localization.srv import *



def call_service():
    # rospy.init_node('test_node', anonymous=True)
    # rospy.wait_for_service('global_localization')

    # try:
    #     #create handler to call the service
    #     globalSrv = rospy.ServiceProxy('global_localization')
    #     print("server proxy success!!!")
    print("hello")
        

if __name__ == '__main__':
    try:
        call_service()
    except rospy.ROSInterruptException:
        pass
