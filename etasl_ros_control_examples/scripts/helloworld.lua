-- require("context")

-- local r = u:getExpressions(ctx)

-- netft_data = ctx:createInputChannelWrench("netft_data")


print(netft_data)
print("Hello, World")

y=4;
print(y)


deg2rad = math.pi / 180.0


z = -90 * deg2rad
x = 0 * deg2rad

-- -- Build a timer to switch between axes.
-- local clock = os.clock
-- function sleep(n) -- seconds
--     local t0 = clock()
--     while clock() - t0 <= n do 
--         axis = z
--     else
--         axis = x 
--     end
-- end

print(z)
print(x)
print(clock)

-- make a wrech
wrench = {}
for i=1,6 do
    wrench[i] = 2+i
end 

print(wrench)
print(wrench[3])