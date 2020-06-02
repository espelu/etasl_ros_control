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

-- netft_data = ctx:createInputChannelWrench("netft_data")

-- meas_tx = ctx:createInputChannelScalar("meas_tx");
-- meas_ty = ctx:createInputChannelScalar("meas_ty");
-- meas_tz = ctx:createInputChannelScalar("meas_tz");
meas_tx = constant(0)
meas_ty = constant(1.0)
meas_tz = constant(0)
-- print(meas_tx)

-- Torque constraints - how to rotate? rotate_x
Constraint{
    context = ctx,
    name    = "tx_control",
    expr    = robot_ee*rotate_x(meas_tx)
    target  = constant(0), --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}
Constraint{
    context = ctx,
    name    = "tx_control",
    expr    = robot_ee*rotate_y(meas_ty)
    target  = constant(0), --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}
Constraint{
    context = ctx,
    name    = "tx_control",
    expr    = robot_ee*rotate_z(meas_tz)
    target  = constant(0), --Tdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}
-- Constraint{
--     context = ctx,
--     name    = "tx_control",
--     model   = unit_x(frame(robot_ee)),--unit_x(rotation(robot_ee)), --ROLL .Want to rotate about x-axis. rot_x?
--     meas    = meas_tx, --measured torque
--     target  = constant(0), --Tdes_ee, 
--     priority= 2,
--     K       = 0.001 --1/Damping constant
-- }

-- Constraint{
--     context = ctx,
--     name    = "ty_control",
--     model   = unit_y(frame(robot_ee)),--unit_y(rotation(robot_ee)), --Pitch. Want to rotate about y-axis. rox_y?
--     meas    = meas_ty, --measured torque
--     target  = constant(0), --Tdes_ee, 
--     priority= 2,
--     K       = 0.001 --1/Damping constant
-- }

-- Constraint{
--     context = ctx,
--     name    = "tz_control",
--     model   = unit_z(frame(robot_ee)),--unit_z(rotation(robot_ee)), --Yaw .Want to rotate about z-axis. rot_z?
--     meas    = meas_tz, --measured torque
--     target  = constant(0), --Tdes_ee, 
--     priority= 2,
--     K       = 0.001 --1/Damping constant
-- }

-- ctx:setOutputExpression("error_tx", meas_tx - 0)
-- ctx:setOutputExpression("error_ty", meas_ty - 0)
-- ctx:setOutputExpression("error_tz", meas_tz - 0)


