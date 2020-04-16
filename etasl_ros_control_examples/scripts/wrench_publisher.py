#!/usr/bin/env python

#  Copyright (c) 2019 Norwegian University of Science and Technology
#  Use of this source code is governed by the LGPL-3.0 license, see LICENSE

import time
import rospy
import numpy as np

from geometry_msgs.msg import WrenchStamped # Wrenchstamped = Wrench, Vector3
from std_msgs.msg import Float64, Header

class ForceMonitor(object):
    def __init__(self, fx_pub, fy_pub, fz_pub):
        self._fx_pub = fx_pub
        self._fy_pub = fy_pub
        self._fz_pub = fz_pub

    def callback(self, msg): 
        meas_fx = msg.wrench.force.x
        meas_fy = msg.wrench.force.y
        meas_fz = msg.wrench.force.z
        meas_tx = msg.wrench.torque.x
        meas_ty = msg.wrench.torque.y
        meas_tz = msg.wrench.torque.z

        self._fx_pub.publish(meas_fx)
        self._fy_pub.publish(meas_fy)
        self._fz_pub.publish(meas_fz)
        rospy.loginfo('meas_fx: {}, meas_fy: {}, meas_fz: {}, meas_tx: {}, meas_ty: {}, meas_tz: {}'.format(meas_fx, meas_fy, meas_fz, meas_tx, meas_ty, meas_tz))


def wrench_publisher():
    rospy.init_node('wrench_publisher')  
    
    # Defining wrench elements as scalars
    fx_pub = rospy.Publisher('etasl_controller/meas_fx', Float64, queue_size=3)
    fy_pub = rospy.Publisher('etasl_controller/meas_fy', Float64, queue_size=3)
    fz_pub = rospy.Publisher('etasl_controller/meas_fz', Float64, queue_size=3)
    tx_pub = rospy.Publisher('etasl_controller/meas_tx', Float64, queue_size=3)
    ty_pub = rospy.Publisher('etasl_controller/meas_ty', Float64, queue_size=3)
    tz_pub = rospy.Publisher('etasl_controller/meas_tz', Float64, queue_size=3)
    
    monitor_f = ForceMonitor(fx_pub, fy_pub, fz_pub)

    rospy.Subscriber("/netft_data", WrenchStamped, monitor_f.callback)
    rospy.spin()
   

if __name__ == "__main__":
    try:
        wrench_publisher()
        #while not rospy.is_shutdown():
            #wrench_publisher()          
    except rospy.ROSInterruptException:
        pass 
