from math import pi
config = {
    'JOINTS_RADIUS_RANGE':{
        1:(-pi/2, pi/2),
        2:(-pi, 0), #保持屁股翘起
        3:(0, 9*pi/10), #防止舵机反转
        4:(-2*pi/3, pi/3),
        5:(-pi/2, pi/2),
        6:(-pi/2, pi/2)
    },
    'DEFAULT_JOINT_RADIUS': (0, -3*pi/4, pi/2, -pi/4, 0, 0), # 默认的关节弧度

    #连杆长度
    'LINK2': 0.09994,
    'LINK3': 0.09994,
    'LINK4': 0.06264,

    #舵机通道
    'CHANNEL':(0,      1,      2,      3,     4,     5)
             #joint1  joint2  joint3  joint4 joint5  joint6
}
# '''
#         1:(-3*pi/4, 3*pi/4),
#         2:(-pi, -pi/2), #保持屁股翘起
#         3:(-5*pi/6, -pi/18), #防止舵机反转
#         4:(-pi/2, pi/2)
# '''