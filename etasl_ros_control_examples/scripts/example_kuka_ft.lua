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

netft_data = ctx:createInputChannelWrench("netft_data")

-- meas_fx = ctx:createInputChannelScalar("meas_fx")
-- meas_fy = ctx:createInputChannelScalar("meas_fy")
-- meas_fz = ctx:createInputChannelScalar("meas_fz")
-- meas_tx = ctx:createInputChannelScalar("meas_tx")
-- meas_ty = ctx:createInputChannelScalar("meas_ty")
-- meas_tz = ctx:createInputChannelScalar("meas_tz")

-- netft_data[1] is the same as coord_x(force(netft_data)))??
-- Force constraints
Constraint{
    context = ctx,
    name    = "fx_control",
    model   = coord_x(origin(robot_ee)),
    meas    = netft_data[1],--meas_fx, --Fmeas_ee,a
    target  = constant(0), --Fdes_ee,
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "fy_control",
    model   = coord_y(origin(robot_ee)),
    meas    = netft_data[2],--meas_fy, --Fmeas_ee,
    target  = 0, --Fdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "fz_control",
    model   = coord_z(origin(robot_ee)),
    meas    = netft_data[3],--meas_fz, --Fmeas_ee,
    target  = 0, --Fdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

-- Torque constraints - incuded in separate .lua file?

Constraint{
    context = ctx,
    name    = "tx_control",
    model   = rotate_x(frame(robot_ee)), --ROLL .Want to rotate about x-axis. rot_x?
    meas    = netft_data[4],--meas_tx, --measured torque
    target  = 0, --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "ty_control",
    model   = rotate_y(frame(robot_ee)), --Pitch. Want to rotate about y-axis. rox_y?
    meas    = netft_data[5],--meas_ty, --measured torque
    target  = 0, --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "tz_control",
    model   = rotate_z(frame(robot_ee)), --Yaw .Want to rotate about z-axis. rot_z?
    meas    = netft_data[6],--meas_tz, --measured torque
    target  = 0, --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

-- ctx:setOutputExpression("error_fx", meas_fx - 0)
-- ctx:setOutputExpression("error_fy", meas_fy - 0)
-- ctx:setOutputExpression("error_fz", meas_fz - 0)
-- ctx:setOutputExpression("error_tx", meas_tx - 0)
-- ctx:setOutputExpression("error_ty", meas_ty - 0)
-- ctx:setOutputExpression("error_tz", meas_tz - 0)



