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


meas_fx = ctx:createInputChannelScalar("meas_fx")
meas_fy = ctx:createInputChannelScalar("meas_fy")
meas_fz = ctx:createInputChannelScalar("meas_fz")


-- Force constraints
Constraint{
    context = ctx,
    name    = "fx_control",
    model   = coord_x(origin(robot_ee)),
    meas    = meas_fx, --Fmeas_ee,a
    target  = constant(0), --Fdes_ee,
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "fy_control",
    model   = coord_y(origin(robot_ee)),
    meas    = meas_fy, --Fmeas_ee,
    target  = 0, --Fdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}

Constraint{
    context = ctx,
    name    = "fz_control",
    model   = coord_z(origin(robot_ee)),
    meas    = meas_fz, --Fmeas_ee,
    target  = 0, --Fdes_ee, 
    priority= 2,
    K       = 0.001 --1/Damping constant
}



ctx:setOutputExpression("error_fx", meas_fx - 0)
ctx:setOutputExpression("error_fy", meas_fy - 0)
ctx:setOutputExpression("error_fz", meas_fz - 0)



