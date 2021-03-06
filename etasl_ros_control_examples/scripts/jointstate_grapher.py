#!/usr/bin/env python3

#  Copyright (c) 2019 Norwegian University of Science and Technology
#  Use of this source code is governed by the LGPL-3.0 license, see LICENSE
#  Builds on Dag Lofthus code

import numpy as np
import matplotlib
from matplotlib import pyplot as plt

import rospy
from sensor_msgs.msg import JointState

joint_pos = []
# joint_vel = []
i = 0

def jointstate_clbk(data):
    global joint_pos
    # global joint_vel
    global i

    joint_pos.append(data.position)
    # joint_vel.append(data.velocity)

    if i == 10000:
        joint_pos_plot = np.array(joint_pos)
        # joint_vel_plot = np.array(joint_vel)

        plt.figure(1)
        #plt.subplot(611)
        plt.plot(joint_pos_plot[:,0],'b',linewidth=0.1)
        #plt.subplot(612)
        plt.plot(joint_pos_plot[:,1],'g',linewidth=0.1)
        #plt.subplot(613)
        plt.plot(joint_pos_plot[:,2],'r',linewidth=0.1)
        #plt.subplot(614)
        plt.plot(joint_pos_plot[:,3],'y',linewidth=0.1)
        #plt.subplot(615)
        plt.plot(joint_pos_plot[:,4],'c',linewidth=0.1)
        #plt.subplot(616)
        plt.plot(joint_pos_plot[:,5],'m',linewidth=0.1)
        plt.savefig('/home/plots/joint_pos.svg')

        # plt.figure(2)
        # #plt.subplot(611)
        # plt.plot(joint_vel_plot[:,0],'b',linewidth=0.1)
        # #plt.subplot(612)
        # plt.plot(joint_vel_plot[:,1],'g',linewidth=0.1)
        # #plt.subplot(613)
        # plt.plot(joint_vel_plot[:,2],'r',linewidth=0.1)
        # #plt.subplot(614)
        # plt.plot(joint_vel_plot[:,3],'y',linewidth=0.1)
        # #plt.subplot(615)
        # plt.plot(joint_vel_plot[:,4],'c',linewidth=0.1)
        # #plt.subplot(616)
        # plt.plot(joint_vel_plot[:,5],'m',linewidth=0.1)
        # plt.savefig('/home/plots/joint_vel.svg')
    i += 1

def listener():
    rospy.init_node('jointstate_grapher')
    
    # rospy.Subscriber('/etasl_controller_2/joint_states_realtime', JointState, jointstate_clbk)
    # rospy.Subscriber('/etasl_controller_calib/joint_states_realtime', JointState, jointstate_clbk)
    # rospy.Subscriber('/etasl_controller_force/joint_states_realtime', JointState, jointstate_clbk)
    # rospy.Subscriber('/etasl_controller/joint_states_realtime', JointState, jointstate_clbk)
    rospy.Subscriber('/joint_states', JointState, jointstate_clbk)
    # rospy.Subscriber('/etasl_controller_4/joint_states_realtime', JointState, jointstate_clbk)
    # rospy.Subscriber('/etasl_controller_lissajous/joint_states_realtime', JointState, jointstate_clbk)
    # rospy.Subscriber('/etasl_controller_home/joint_states_realtime', JointState, jointstate_clbk)

    rospy.spin()

if __name__ == "__main__":
    listener()