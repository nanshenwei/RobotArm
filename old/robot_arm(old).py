import math
from math import sin, cos
from configs import config
import random

class R_robot:
    L2 = config['LINK2']
    L3 = config['LINK3']
    L4 = config['LINK4']

    MAX_INTIAL_PHI_TIME = 100000   #最大尝试次数

    def __init__(self, is_debug=False):
        self.is_debug = is_debug

    def is_vertical_joint_radius(self, candi_joint_radius):
        (theta2, theta3, theta4) = candi_joint_radius[2:]
        radius = list(filter(None, [theta2, theta3, theta4]))
        radius.append(2*math.pi)
        if sum(radius) < 15*math.pi/36 or sum(radius) > 21*math.pi/36:
            return False
        return True

    def is_legal_joint_radius(self, candi_joint_radius):
        '''判断关节角度是否合法'''
        for joint_num in range(1, len(candi_joint_radius)):
            (min_radius, max_radius) = config['JOINTS_RADIUS_RANGE'][joint_num]
            if candi_joint_radius[joint_num] is None:
                continue
            elif candi_joint_radius[joint_num] < min_radius or candi_joint_radius[joint_num] > max_radius:
                return False
        return True

    def is_right_solution(self, x, y, z, theta1, theta2, theta3, theta4):
        '''通过正向运动学，确认逆向运动学的解是否正确'''
        nx = cos(theta1)*(self.L2*cos(theta2)+self.L3*cos(theta2+theta3)+self.L4*cos(theta2+theta3+theta4))
        ny = sin(theta1)*(self.L2*cos(theta2)+self.L3*cos(theta2+theta3)+self.L4*cos(theta2+theta3+theta4))
        nz = -(self.L2*sin(theta2)+self.L3*sin(theta2+theta3)+self.L4*sin(theta2+theta3+theta4))
        if abs(x-nx) > 1e-3 or abs(y-ny) > 1e-3 or abs(z-nz) > 1e-3:
            return False
        return True

    def inverse_kinematics(self, wx, wy, wz):
        '''逆向运动学'''
        candi_joints = [] #候选关节

        #计算目标点距离是否合法
        distance = math.sqrt(wx**2 + wy**2 + wz**2)
        if distance > self.L2 + self.L3 + self.L4:
            if self.is_debug:
                print('[ERROR]距离超出机械臂范围')
            return False, None
        #############################
        ##    Joint1旋转弧度求解    ##
        #############################
        if wx == 0 and wy == 0:
            min_radius1, max_radius1 = config['JOINTS_RADIUS_RANGE'][1]
            theta1 = random.uniform(min_radius1, max_radius1)
            candi_joints.append([None, theta1, None, None, None])
        else:
            theta1 = math.atan2(wy, wx)
            candi_joints.append([None, theta1, None, None, None])

            theta1 = math.atan2(-wy, -wx)
            candi_joints.append([None, theta1, None, None, None])
        #过滤合法的Joint1取值
        candi_joints = list(filter(self.is_legal_joint_radius, candi_joints))
        if len(candi_joints) == 0:
            if self.is_debug:
                print('[ERROR]没有找到合适的theta1')
            return False, None

        #############################
        ##    Joint3旋转弧度求解    ##
        #############################
        min_radius2, max_radius2 = config['JOINTS_RADIUS_RANGE'][2]
        min_radius3, max_radius3 = config['JOINTS_RADIUS_RANGE'][3]
        min_radius4, max_radius4 = config['JOINTS_RADIUS_RANGE'][4]
        min_radius = min_radius2 + min_radius3 + min_radius4
        max_radius = max_radius2 + max_radius3 + max_radius4
        for initial_num in range(self.MAX_INTIAL_PHI_TIME):
            #随机一个phi
            phi = random.gauss((min_radius+max_radius)/2, (max_radius-min_radius)/4)
            #phi = random.uniform(min_radius, max_radius)
            if self.is_debug:
                print('第{}次尝试随机生成phi,phi={}'.format(initial_num, phi))
            tmp_candi_joints = []
            for candi in candi_joints:
                theta1 = candi[1]
                a = wx/cos(theta1) if wx != 0 else wy/sin(theta1)
                b = a - self.L4 * cos(phi)
                z = wz + self.L4 * sin(phi)

                cos_theta3 = (z**2 + b**2 - self.L2**2 - self.L3**2)/(2*self.L2 * self.L3)
                #对cos(theta3)的范围进行检查
                if abs(cos_theta3) > 1:
                    if self.is_debug:
                        print('[INFO]非法cos(theta3),重新生成phi')
                    continue
                sin_theta3 = math.sqrt(1 - cos_theta3**2)
                #情况1: sin(theta3) > 0
                #不存在情况1
                # theta3 = math.atan2(sin_theta3, cos_theta3)
                # tmp_candi_joints.append([None, theta1, None, theta3, None])
                #情况2: sin(theta3) < 0
                theta3 = math.atan2(-sin_theta3, cos_theta3)
                tmp_candi_joints.append([None, theta1, None, theta3, None])
            #对Joint3的弧度进行筛选
            tmp_candi_joints = list(filter(self.is_legal_joint_radius, tmp_candi_joints))
            if len(tmp_candi_joints) == 0:
                continue

            #############################
            ##Joint2与Joint4旋转弧度求解##
            #############################
            for i_candi in range(len(tmp_candi_joints)):
                candi = tmp_candi_joints[i_candi]
                theta3 = candi[3]
                k1 = self.L2 + self.L3 * cos(theta3)
                k2 = self.L3 * sin(theta3)
                theta2 = math.atan2(-z, b) - math.atan2(k2, k1)
                theta4 = phi - theta2 - theta3
                candi[2] = theta2
                candi[4] = theta4

            #对Joint2跟Joint4的弧度进行筛选
            tmp_candi_joints = list(filter(self.is_legal_joint_radius, tmp_candi_joints))
            #tmp_candi_joints = list(filter(self.is_vertical_joint_radius, tmp_candi_joints))
            #根据正向运动学再次确认解是否正确
            tmp_candi_joints = list(filter(lambda candi: self.is_right_solution(wx, wy, wz, candi[1], candi[2], candi[3], candi[4]), tmp_candi_joints))

            if len(tmp_candi_joints) == 0:
                continue
            else:
                #只是把众多解取第一元素
                return True, tmp_candi_joints
        if self.is_debug:
            print('[ERROR] 尝试{}次后没有找到关节角度'.format(self.MAX_INTIAL_PHI_TIME))
        return False, None

if __name__ == "__main__":
    import numpy
    arm = R_robot(is_debug=False)
    
    for i in numpy.arange(0.01,0.20,0.01):
        ret, reu = arm.inverse_kinematics(0,0,i)
        if ret:
            print('{}xxxxxxxxx{}xxxxxxxxx{}'.format(ret, reu, i))
    
    '''
    ret, reu = arm.inverse_kinematics(0,0,0.16)
    if ret:
        print('{}xxxxxxxxx{}'.format(ret, reu))
    '''
