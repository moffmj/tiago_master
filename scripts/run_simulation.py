#!/usr/bin/env python

import rospy
import roslaunch
import subprocess
#import pick_client


#package = 'matt_test_package'
#executable = 'pick_demo.launch'
#node = roslaunch.core.Node(package, executable)

#launch = roslaunch.scriptapi.ROSLaunch()
#launch.start()

#process = launch.launch(node)
#print process.is_alive()
#process.stop()

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
	
	print("start")
	subprocess.call("./run_gui.sh", shell=True)
	print("end")

