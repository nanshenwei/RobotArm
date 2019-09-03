import command
import math
import time

Cmd = command.Cmd()
a = input()
#1 初始 
#+    左转 站 下探 低垂 左扭 逆时
#     朝向 腿 身子 抬头 扭头 歪头
#-    右转 蹲 挺起 抬高 右扭 顺时
# Cmd.goJ(70,-150,140,-85,0,0,radius=0)
# a = input()
# #2 扭头
# Cmd.goJ(70,-150,140,-85,-90,0,radius=0)
# time.sleep(.8)
# Cmd.goJ(70,-150,140,-85,-90,30,radius=0)
# Cmd.goJ(70,-150,140,-85,-90,-30,radius=0)
# Cmd.goJ(70,-150,140,-85,-90,0,radius=0)
# time.sleep(1)
#3 头不动）转身
Cmd.goJ(0,-150,140,-85,0,0,radius=0)
#------------------------------------
a = input()



# #4 摇摆
Cmd.step_l = 10
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,0,0,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,0,0,radius=0)
time.sleep(.08)

# #5
Cmd.step_l = 65
print("扭头")
Cmd.goJ(-45,-150,140,-85,45,0,radius=0)
Cmd.step_l = 10
a = input()
print("继续摇")
Cmd.step_l = 65
Cmd.goJ(-45,-150,140,-85,45,15,radius=0)
Cmd.step_l = 10

Cmd.goJ(-45,-145,132,-85,45,15,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,45,15,radius=0)
time.sleep(.08)

Cmd.step_l = 65
Cmd.goJ(-45,-150,140,-85,45,-20,radius=0)
Cmd.step_l = 10
Cmd.goJ(-45,-145,132,-85,45,-20,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,45,-20,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,45,-20,radius=0)
time.sleep(.065)

Cmd.step_l = 65
Cmd.goJ(-45,-150,140,-85,45,15,radius=0)
Cmd.step_l = 10
Cmd.goJ(-45,-150,140,-85,45,15,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,45,15,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,45,15,radius=0)
time.sleep(.08)

Cmd.step_l = 65
Cmd.goJ(-45,-150,140,-85,45,25,radius=0)
Cmd.step_l = 10
Cmd.goJ(-45,-145,132,-85,45,25,radius=0)
time.sleep(.065)

Cmd.step_l = 65
Cmd.goJ(-45,-145,132,-85,45,20,radius=0)
Cmd.step_l = 10

Cmd.goJ(-45,-150,140,-85,45,20,radius=0)
time.sleep(.08)
Cmd.goJ(-45,-145,132,-85,45,20,radius=0)
time.sleep(.065)
Cmd.goJ(-45,-150,140,-85,45,20,radius=0)
time.sleep(.08)

Cmd.step_l = 65
Cmd.goJ(-45,-150,140,-85,45,-15,radius=0)
Cmd.step_l = 10
Cmd.goJ(-45,-145,132,-85,45,-15,radius=0)
time.sleep(.065)

print("朝向开始动")
Cmd.step_l_0 = 50
Cmd.step_l = 65
Cmd.goJ(-35,-145,132,-85,35,15,radius=0)
Cmd.step_l = 10

Cmd.goJ(-35,-150,140,-85,35,15,radius=0)
time.sleep(.08)
Cmd.step_l = 65
Cmd.goJ(-35,-150,140,-85,35,-15,radius=0)
Cmd.step_l = 10
Cmd.goJ(-35,-145,132,-85,35,-15,radius=0)
time.sleep(.065)
Cmd.goJ(-35,-150,140,-85,35,-15,radius=0)
time.sleep(.08)

Cmd.step_l = 65
Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
Cmd.step_l = 10

Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
time.sleep(.065)
Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
time.sleep(.08)
Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
time.sleep(.065)
Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
time.sleep(.08)
Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
time.sleep(.065)
Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
time.sleep(.08)
Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
time.sleep(.065)
Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
time.sleep(.08)

Cmd.step_l = 65
Cmd.goJ(-35,-145,132,-85,45,-15,radius=0)
Cmd.step_l = 10

Cmd.goJ(-35,-145,132,-85,45,-15,radius=0)
time.sleep(.065)
Cmd.goJ(--35,-150,140,-85,45,-15,radius=0)
time.sleep(.08)
Cmd.step_l = 65
Cmd.goJ(20,-145,132,-85,-20,-20,radius=0)
Cmd.step_l = 10

Cmd.goJ(20,-145,132,-85,-20,20,radius=0)
time.sleep(.065)
#############################################################
# Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
# time.sleep(.08)
# Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
# time.sleep(.065)
# Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
# time.sleep(.08)
# Cmd.goJ(-35,-145,132,-85,45,20,radius=0)
# time.sleep(.065)
# Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
# time.sleep(.08)

# Cmd.goJ(40,-145,132,-85,-40,20,radius=0)
# time.sleep(.065)
# Cmd.goJ(40,-150,140,-85,-40,20,radius=0)
# time.sleep(.08)
# Cmd.goJ(40,-145,132,-85,-40,20,radius=0)
# time.sleep(.065)
# Cmd.goJ(-35,-150,140,-85,45,20,radius=0)
# time.sleep(.08)

Cmd.step_l = 65
Cmd.goJ(45,-145,132,-85,-45,10,radius=0)
time.sleep(.065)
Cmd.step_l = 10

# Cmd.goJ(40,-150,140,-85,-35,10,radius=0)
# time.sleep(.08)
# Cmd.goJ(45,-145,132,-85,-45,0,radius=0)
# time.sleep(.065)
# Cmd.goJ(45,-150,140,-85,-45,0,radius=0)
# time.sleep(.08)
# Cmd.goJ(45,-145,132,-85,-45,-5,radius=0)
# time.sleep(.065)

# Cmd.goJ(15,-150,140,-85,-35,-5,radius=0)
# time.sleep(.08)
# Cmd.goJ(15,-145,132,-85,-35,-5,radius=0)
# time.sleep(.065)
# Cmd.goJ(15,-150,140,-85,-15,0,radius=0)
# time.sleep(.08)
# Cmd.goJ(15,-145,132,-85,-15,0,radius=0)
# time.sleep(.065)
# Cmd.goJ(15,-150,140,-85,-10,0,radius=0)
# time.sleep(.08)
################################################################
# #6
# Cmd.goJ(-60,-60,60,-15,0,-90,radius=0)
# time.sleep(1)
# a = input()
# Cmd.step_l_0 = 60
# Cmd.goJ(60,-60,60,-15,0,-90,radius=0)
# time.sleep(1)
# a = input()
# Cmd.goJ(-60,-60,60,-15,0,-90,radius=0)