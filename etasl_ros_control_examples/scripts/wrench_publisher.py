#!/usr/bin/env python

#  Copyright (c) 2019 Norwegian University of Science and Technology
#  Use of this source code is governed by the LGPL-3.0 license, see LICENSE

import time
import rospy
import numpy as np

from geometry_msgs.msg import WrenchStamped # Wrenchstamped = Wrench, Vector3
from std_msgs.msg import Float64, Header

# class BiasSensor(object):

#     def importData(self, msg): #force_x, force_y,  n, t
#             global netft_matrix
#             t_end=time.time() + 3
#             n=20
#             netft_matrix = np.zeros((6,n))
#             i=0
#             while time.time() < t_end:
#                 netft_matrix [0,i] = msg.wrench.force.x # meas_fx #fx
#                 netft_matrix [1,i] = msg.wrench.force.y # meas_fy #fy
#                 netft_matrix [2,i] = msg.wrench.force.z # meas_fz
#                 netft_matrix [3,i] = msg.wrench.torque.x #meas_tx
#                 netft_matrix [4,i] = msg.wrench.torque.y #meas_ty
#                 netft_matrix [5,i] = msg.wrench.torque.z #meas_tz
#                 i += 1
#                 pass
#             print(netft_matrix)
#             #return netft_matrix
#             pass

#     def vectorCalculator(self,netft_matrix):
#             global mean
#             
#             mean = np.zeros((6,1))
#             std_dev = np.zeros((6,1))
#             var = np.zeros((6,1))
#             for i in range(6):  
#                 mean[i] = np.mean(netft_matrix[i])
#                 std_dev[i]= np.nanstd(netft_matrix[i])
#                 var[i] = np.var(netft_matrix[i])
                
#                 pass
#             print("mean values - ", mean)
#             print("standard deviation - ", std_dev)
#             print("variances - ", var)    

def importData(msg): #force_x, force_y,  n, t
    #rospy.Subscriber("/netft_data", WrenchStamped)
    global netft_matrix
    #t_end=time.time() + 3
    n=20
    netft_matrix = np.zeros((6,n))
    i=0
    while i < n:#time.time() < t_end:
        netft_matrix [0,i] = msg.wrench.force.x # meas_fx #fx
        netft_matrix [1,i] = msg.wrench.force.y # meas_fy #fy
        netft_matrix [2,i] = msg.wrench.force.z # meas_fz
        netft_matrix [3,i] = msg.wrench.torque.x #meas_tx
        netft_matrix [4,i] = msg.wrench.torque.y #meas_ty
        netft_matrix [5,i] = msg.wrench.torque.z #meas_tz
        i += 1
        pass
    #print(netft_matrix)
    return netft_matrix


# def vectorCalculator(msg):#self,netft_matrix):
#     global netft_matrix
#     #t_end=time.time() + 3
#     n=20
#     netft_matrix = np.zeros((6,n))
#     i=0
#     while i < n:#time.time() < t_end:
#         netft_matrix [0,i] = msg.wrench.force.x # meas_fx #fx
#         netft_matrix [1,i] = msg.wrench.force.y # meas_fy #fy
#         netft_matrix [2,i] = msg.wrench.force.z # meas_fz
#         netft_matrix [3,i] = msg.wrench.torque.x #meas_tx
#         netft_matrix [4,i] = msg.wrench.torque.y #meas_ty
#         netft_matrix [5,i] = msg.wrench.torque.z #meas_tz
#         i += 1
#         pass
#     # ft_matrix = importData()
    # rospy.Subscriber("/netft_data", WrenchStamped, ft_matrix)
    # global mean
    # mean = np.zeros((6,1))
    # mean[0]=2
    # mean[1]=2
    # mean[2]=2
    # mean[3]=2
    # mean[4]=2
    # mean[5]=2
    # mean = np.zeros((6,1))
    # std_dev = np.zeros((6,1))
    # var = np.zeros((6,1))
    # for i in range(6):  
    #     mean[i] = np.mean(netft_matrix[i])
    #     std_dev[i]= np.nanstd(netft_matrix[i])
    #     var[i] = np.var(netft_matrix[i])
            
    #     pass
    # print("mean values - ", mean)
    # print("standard deviation - ", std_dev)
    # print("variances - ", var)
    # return mean 

class ForceMonitor(object):
    #mean = np.zeros((6,1))
    #netft_matrix = np.zeros((6,20))

    def __init__(self, fx_pub, fy_pub, fz_pub, tx_pub, ty_pub, tz_pub):
        self._fx_pub = fx_pub
        self._fy_pub = fy_pub
        self._fz_pub = fz_pub
        self._tx_pub = tx_pub
        self._ty_pub = ty_pub
        self._tz_pub = tz_pub   

    def importData(self,msg): #force_x, force_y,  n, t
        n=20
        ForceMonitor.netft_matrix = np.ones((6,n))
        #t_end=time.time() + 3
        
        i=0
        while i < n:#time.time() < t_end:
            ForceMonitor.netft_matrix [0,i] = msg.wrench.force.x # meas_fx #fx
            ForceMonitor.netft_matrix [1,i] = msg.wrench.force.y # meas_fy #fy
            ForceMonitor.netft_matrix [2,i] = msg.wrench.force.z # meas_fz
            ForceMonitor.netft_matrix [3,i] = msg.wrench.torque.x #meas_tx
            ForceMonitor.netft_matrix [4,i] = msg.wrench.torque.y #meas_ty
            ForceMonitor.netft_matrix [5,i] = msg.wrench.torque.z #meas_tz
            i += 1
            pass
        #print(netft_matrix)
        #return netft_matrix

    def vectorCalculator(self):
        global mean
        mean = np.zeros((6,1))
        mean[0]=69
        mean[1]=69
        mean[2]=69
        mean[3]=69
        mean[4]=69
        mean[5]=69
    
        # std_dev = np.zeros((6,1))
        # var = np.zeros((6,1))
        # for i in range(6):  
        #     mean[i] = np.mean(ForceMonitor.netft_matrix[i])
        #     std_dev[i]= np.nanstd(netft_matrix[i])
        #     var[i] = np.var(netft_matrix[i])
                
        #     pass
        # print("mean values - ", mean)
        # print("standard deviation - ", std_dev)
        # print("variances - ", var)  
        return mean  

    def callback(self, msg): 
       
        meas_fx = msg.wrench.force.x -6#- mean[0]
        meas_fy = msg.wrench.force.y #- mean[1]
        meas_fz = msg.wrench.force.z #- mean[2]
        meas_tx = msg.wrench.torque.x #- mean[3]
        meas_ty = msg.wrench.torque.y #- mean[4]
        meas_tz = msg.wrench.torque.z - mean[5]#- mean[5]

        self._fx_pub.publish(meas_fx)
        self._fy_pub.publish(meas_fy)
        self._fz_pub.publish(meas_fz)
        self._tx_pub.publish(meas_tx)
        self._ty_pub.publish(meas_ty)
        self._tz_pub.publish(meas_tz)
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
    
    monitor_f = ForceMonitor(fx_pub, fy_pub, fz_pub, tx_pub, ty_pub, tz_pub)


    rospy.Subscriber("/netft_data", WrenchStamped, monitor_f.callback)
    rospy.spin()
   

if __name__ == "__main__":
    try:
        # count=0
        # if count ==0:
        #     ForceMonitor.importData(msg) #finn mean
        #     ForceMonitor.vectorCalculator(netft_matrix)
        #     count +=1
        #     pass
        #importData("/netft_data")
        #vectorCalculator()
        mean = ForceMonitor(vectorCalculator())
        wrench_publisher()
        
        #while not rospy.is_shutdown():
            #wrench_publisher()          
    except rospy.ROSInterruptException:
        pass 

 

