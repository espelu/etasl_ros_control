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

calib_wrench = ctx:createInputChannelWrench("calib_wrench")

-- Force constraints
Constraint{
    context = ctx,
    name    = "fx_control",
    model   = coord_x(origin(robot_ee)),
    meas    = calib_wrench[1], --Fmeas_ee,a
    target  = constant(0), --Fdes_ee,
    priority= 2,
    K       = 0.001 --Usikker på K
}

Constraint{
    context = ctx,
    name    = "fy_control",
    model   = coord_y(origin(robot_ee)),
    meas    = calib_wrench[2], --Fmeas_ee,
    target  = 0, --Fdes_ee, 
    priority= 2,
    K       = 0.001 --Usikker på K
}

Constraint{
    context = ctx,
    name    = "fz_control",
    model   = coord_z(origin(robot_ee)),
    meas    = calib_wrench[3], --Fmeas_ee,
    target  = 0, --Fdes_ee, 
    priority= 2,
    K       = 0.001 --Usikker på K
}

ctx:setOutputExpression("error_fx", calib_wrench[1] - 0)
ctx:setOutputExpression("error_fy", calib_wrench[2] - 0)
ctx:setOutputExpression("error_fz", calib_wrench[3] - 0)


-- -- meas_fx = ctx:createInputChannelScalar("etasl_controller/meas_fx") --/etasl_controller/
-- -- meas_fy = ctx:createInputChannelScalar("etasl_controller/meas_fy")
-- -- meas_fz = ctx:createInputChannelScalar("etasl_controller/meas_fz")
-- -- fx = constant(10)
-- -- fy = constant(10)
-- -- fz = constant(10)

-- -- Force constraints
-- Constraint{
--     context = ctx,
--     name    = "fx_control",
--     model   = coord_x(origin(robot_ee)),
--     meas    = meas_fx, --Fmeas_ee,a
--     target  = constant(0), --Fdes_ee,
--     priority= 2,
--     K       = 0.001 --1/Damping constant
-- }

-- Constraint{
--     context = ctx,
--     name    = "fy_control",
--     model   = coord_y(origin(robot_ee)),
--     meas    = meas_fy, --Fmeas_ee,
--     target  = constant(0), --Fdes_ee, 
--     priority= 2,
--     K       = 0.001 --1/Damping constant
-- }

-- Constraint{
--     context = ctx,
--     name    = "fz_control",
--     model   = coord_z(origin(robot_ee)),
--     meas    = meas_fz, --Fmeas_ee,
--     target  = constant(0), --Fdes_ee, 
--     priority= 2,
--     K       = 0.001 --1/Damping constant
-- }



-- ctx:setOutputExpression("error_fx", meas_fx - 0)
-- ctx:setOutputExpression("error_fy", meas_fy - 0)
-- ctx:setOutputExpression("error_fz", meas_fz - 0)



