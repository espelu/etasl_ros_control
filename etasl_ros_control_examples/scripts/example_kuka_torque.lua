-- Copyright (c) 2019 Norwegian University of Science and Technology
-- Use of this source code is governed by the LGPL-3.0 license, see LICENSE

require("context")
require("geometric")

local u = UrdfExpr()
u:readFromParam("/robot_description")
u:addTransform("ee", "tool0", "base_link")

local r = u:getExpressions(ctx)

-- The transformation of the robot mounting plate frame with respect to the robot base frame
robot_ee = r.ee

-- The name of the robot joints
robot_joints = {
    "joint_a1",
    "joint_a2",
    "joint_a3",
    "joint_a4",
    "joint_a5",
    "joint_a6"
}

-- meas_tx = ctx:createInputChannelScalar("msg.wrench.torque.x")
-- meas_ty = ctx:createInputChannelScalar("msg.wrench.torque.y")
-- meas_tz = ctx:createInputChannelScalar("msg.wrench.torque.z")

meas_tx = ctx:createInputChannelScalar("meas_tx");
meas_ty = ctx:createInputChannelScalar("meas_ty");
meas_tz = ctx:createInputChannelScalar("meas_tz");

print(meas_tx)

-- Torque constraints - how to rotate?

Constraint{
    context = ctx,
    name    = "tx_control",
    model   = coord_x(origin(robot_ee)), --ROLL .Want to rotate about x-axis. rot_x?
    meas    = meas_tx, --measured torque
    target  = 0, --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "ty_control",
    model   = coord_y(origin(robot_ee)), --Pitch. Want to rotate about y-axis. rox_y?
    meas    = meas_ty, --measured torque
    target  = 0, --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "tz_control",
    model   = coord_z(origin(robot_ee)), --Yaw .Want to rotate about z-axis. rot_z?
    meas    = meas_tz, --measured torque
    target  = 0, --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

ctx:setOutputExpression("error_tx", meas_tx - 0)
ctx:setOutputExpression("error_ty", meas_ty - 0)
ctx:setOutputExpression("error_tz", meas_tz - 0)


