#!/usr/bin/env python

#  Copyright (c) 2019 Norwegian University of Science and Technology
#  Use of this source code is governed by the LGPL-3.0 license, see LICENSE

import time
import rospy
import numpy as np

from geometry_msgs.msg import WrenchStamped, Wrench 
# Wrenchstamped = Wrench, Vector3
from std_msgs.msg import Float64, Header

import argparse  # To parse the command line input
class BiasSensor(object):
    """Biasing of a wrench found at input_name, outputedd to output_name.
    Averaging is performed over 'averaging_time' seconds.
    """
    def __init__(self, input_name, output_name, averaging_time, publish_stamped=False):
        # Topics to subscribe to and publish to
        self.input_name = input_name
        self.output_name = output_name

        # Use wrench stamped topic? Or just wrench topic?
        self.publish_stamped = publish_stamped

        # Make sure the averaging time is a rospy.Duration object
        if isinstance(averaging_time, rospy.Duration):
            self.averaging_time = averaging_time
        else:
            self.averaging_time = rospy.Duration.from_sec(averaging_time)
        # Prepare average wrench
        self.average_fx = 0.0
        self.average_fy = 0.0
        self.average_fz = 0.0
        self.average_tx = 0.0
        self.average_ty = 0.0
        self.average_tz = 0.0
        # Are we publishing a wrench stamped or a wrench object? (I think etasl needs wrench)
        if self.publish_stamped:
            self.wrench_output = rospy.Publisher(output_name, WrenchStamped, queue_size=1)
        else:
            self.wrench_output = rospy.Publisher(output_name, Wrench)
        # Where do we get the input from?
        self.wrench_input = rospy.Subscriber(input_name, WrenchStamped, self.redirect)
        # Prepare variables
        self.initial_time = None
        self.n_samples = 0.0

    def redirect(self, msg):
        # If this is the first message, initialize time
        if self.initial_time is None:
            self.initial_time = rospy.Time.now()
        # Improve average if we're still in averaging duration
        if rospy.Time.now() - self.initial_time < self.averaging_time:
            # Increase the sample we're at
            self.n_samples += 1
            n = self.n_samples # Just for easier reading
            # Iterative version of calculating the mean
            self.average_fx = self.average_fx*(n-1)/n + msg.wrench.force.x/n
            self.average_fy = self.average_fy*(n-1)/n + msg.wrench.force.y/n
            self.average_fz = self.average_fz*(n-1)/n + msg.wrench.force.z/n
            self.average_tx = self.average_tx*(n-1)/n + msg.wrench.torque.x/n
            self.average_ty = self.average_ty*(n-1)/n + msg.wrench.torque.y/n
            self.average_tz = self.average_tz*(n-1)/n + msg.wrench.torque.z/n

        # Initialize the recalibrated wrench
        if self.publish_stamped:
            new_wrench = WrenchStamped()
            # Copy header stamp from the actual wrench
            new_wrench.header.stamp  = msg.header.stamp
            new_wrench.header.frame_id = msg.header.frame_id
            # Set the wrench values
            new_wrench.wrench.force.x = msg.wrench.force.x - self.average_fx
            new_wrench.wrench.force.y = msg.wrench.force.y - self.average_fy
            new_wrench.wrench.force.z = msg.wrench.force.z - self.average_fz
            new_wrench.wrench.torque.x = msg.wrench.torque.x - self.average_tx
            new_wrench.wrench.torque.y = msg.wrench.torque.y - self.average_ty
            new_wrench.wrench.torque.z = msg.wrench.torque.z - self.average_tz
        else:
            # Set the wrench values directly
            new_wrench = Wrench()
            new_wrench.force.x = msg.wrench.force.x - self.average_fx
            new_wrench.force.y = msg.wrench.force.y - self.average_fy
            new_wrench.force.z = msg.wrench.force.z - self.average_fz
            new_wrench.torque.x = msg.wrench.torque.x - self.average_tx
            new_wrench.torque.y = msg.wrench.torque.y - self.average_ty
            new_wrench.torque.z = msg.wrench.torque.z - self.average_tz
        self.wrench_output.publish(new_wrench)

if __name__ == "__main__":
    rospy.init_node("calibrated_wrench", anonymous=True)
    bs = BiasSensor(
        input_name="netft_data",  # The source WrenchStamped signal
        output_name="calib_wrench",  # whatever output name you want
        averaging_time=5,  # Average the first 5 seconds of data
        publish_stamped=True
    )
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass