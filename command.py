from robot_arm import R_robot
from PCA9685 import PCA9685
from configs import config
import math
import time


# '''
# TODO
# 处理joint与channel的关系。
# '''

class Cmd:
    min_radius1, max_radius1 = config['JOINTS_RADIUS_RANGE'][1]
    min_radius2, max_radius2 = config['JOINTS_RADIUS_RANGE'][2]
    min_radius3, max_radius3 = config['JOINTS_RADIUS_RANGE'][3]
    min_radius4, max_radius4 = config['JOINTS_RADIUS_RANGE'][4]
    min_radius5, max_radius5 = config['JOINTS_RADIUS_RANGE'][5]
    min_radius6, max_radius6 = config['JOINTS_RADIUS_RANGE'][6]
    cur_joint_radius = list(config['DEFAULT_JOINT_RADIUS'])
    (joint1, joint2, joint3, joint4, joint5, joint6) = config['CHANNEL']
    step_l = 30 #步长
    step_l_0 = 20
    delay = 0.02 #减速延时 单位s
    t_pmw = None
# '''
# 以下joint1的舵机都要特殊处理！
# TODO
# joint4要特殊处理！！！！！！！
# '''
    def __init__(self, address=0x40):
        self.act = PCA9685(address=address)
        self.arm = R_robot()
        self.begin()
        self.t_pmw = [self.angle2pwm(self.radius2angle(self.cur_joint_radius[0], 'joint1'), 270),
                      self.angle2pwm(self.radius2angle(self.cur_joint_radius[1], 'joint2')),
                      self.angle2pwm(self.radius2angle(self.cur_joint_radius[2], 'joint3')),
                      self.angle2pwm(self.radius2angle(self.cur_joint_radius[3], 'joint4')),
                      self.angle2pwm(self.radius2angle(self.cur_joint_radius[4], 'joint5')),
                      self.angle2pwm(self.radius2angle(self.cur_joint_radius[5], 'joint6'))]

    def begin(self):
        pwm = [self.angle2pwm(self.radius2angle(self.cur_joint_radius[0], 'joint1'), 270),
               self.angle2pwm(self.radius2angle(self.cur_joint_radius[1], 'joint2')),
               self.angle2pwm(self.radius2angle(self.cur_joint_radius[2], 'joint3')),
               self.angle2pwm(self.radius2angle(self.cur_joint_radius[3], 'joint4')),
               self.angle2pwm(self.radius2angle(self.cur_joint_radius[4], 'joint5')),
               self.angle2pwm(self.radius2angle(self.cur_joint_radius[5], 'joint6'))]
        if not self.t_pmw:
            self.action(self.joint1, pwm[0]) #joint1的舵机是270的
            self.action(self.joint2, pwm[1])
            self.action(self.joint3, pwm[2])
            self.action(self.joint4, pwm[3])
            self.action(self.joint5, pwm[4])
            self.action(self.joint6, pwm[5])
            return True
        self.all_act(pwm)
        return True
        
    def step_act(self, channel, step, step_m, pwm2):
        if step != step_m:
            if channel != 0:
                if self.t_pmw[channel] < pwm2:
                    self.t_pmw[channel] += self.step_l
                    self.action(channel, self.t_pmw[channel])
                if self.t_pmw[channel] > pwm2:
                    self.t_pmw[channel] -= self.step_l
                    self.action(channel, self.t_pmw[channel])
            elif channel == 0:
                if self.t_pmw[channel] < pwm2:
                    self.t_pmw[channel] += self.step_l_0
                    self.action(channel, self.t_pmw[channel])
                if self.t_pmw[channel] > pwm2:
                    self.t_pmw[channel] -= self.step_l_0
                    self.action(channel, self.t_pmw[channel])

    def radius2angle(self, radius, joint):
        if joint == 'joint1':
            return math.degrees(radius) + 135
        elif joint == 'joint2':
        	return math.degrees(radius) + 180
        elif joint == 'joint3':
        	return math.degrees(radius)
        elif joint == 'joint4':
        	return math.degrees(radius) + 120
        elif joint == 'joint5' or joint == 'joint6':
            return math.degrees(radius) + 90

    def angle2pwm(self, angle, servo_angle=180):
        pwm1 = (angle/servo_angle)*2000 + 500
        return pwm1
        
    def goP(self, x, y, z, joint1=1):
        ret, result = self.arm.inverse_kinematics(x, y, z)
        if not ret:
            print('[ERROR] cant find out the point: {}'.format((x, y, z)))
            return False
        (theta1, theta2, theta3, theta4) = result[0][1:] #只取第一个解
        if not self.check_theta(theta1, theta2, theta3, theta4, 0, 0):
            return False
        if not joint1:
            pwm = [self.t_pmw[0], 
                   self.angle2pwm(self.radius2angle(theta2, 'joint2')), 
                   self.angle2pwm(self.radius2angle(theta3, 'joint3')), 
                   self.angle2pwm(self.radius2angle(theta4, 'joint4')),
                   self.t_pmw[4],
                   self.t_pmw[5]]
            self.all_act(pwm)
            return True
        
        pwm = [self.angle2pwm(self.radius2angle(theta1, 'joint1'), 270), 
               self.angle2pwm(self.radius2angle(theta2, 'joint2')), 
               self.angle2pwm(self.radius2angle(theta3, 'joint3')), 
               self.angle2pwm(self.radius2angle(theta4, 'joint4')),
               self.t_pmw[4],
               self.t_pmw[5]]
        self.all_act(pwm)

        return True

    def check_theta(self, theta1, theta2, theta3, theta4, theta5, theta6):
        if theta1 < self.min_radius1 or theta1 > self.max_radius1:
            return False
        if theta2 < self.min_radius2 or theta2 > self.max_radius2:
            return False
        if theta3 < self.min_radius3 or theta3 > self.max_radius3:
            return False
        if theta4 < self.min_radius4 or theta4 > self.max_radius4:
            return False
        if theta5 < self.min_radius5 or theta5 > self.max_radius5:
            return False
        if theta6 < self.min_radius6 or theta6 > self.max_radius6:
            return False
        return True

    def goJ(self, theta1, theta2, theta3, theta4, theta5, theta6, radius=1):
        if not radius:
            theta1 = math.radians(theta1)
            theta2 = math.radians(theta2)
            theta3 = math.radians(theta3)
            theta4 = math.radians(theta4)
            theta5 = math.radians(theta5)
            theta6 = math.radians(theta6)
        if not self.check_theta(theta1, theta2, theta3, theta4, theta5, theta6):
            return False
        # thata = [theta1, theta2, theta3, theta4, theta5, theta6]
        # for t_thata in thata:
        #     if t_thata == No:
        #         print('[ERROR] missing parameter')
        #         return False
        pwm = [self.angle2pwm(self.radius2angle(theta1, 'joint1'), 270), 
               self.angle2pwm(self.radius2angle(theta2, 'joint2')), 
               self.angle2pwm(self.radius2angle(theta3, 'joint3')), 
               self.angle2pwm(self.radius2angle(theta4, 'joint4')), 
               self.angle2pwm(self.radius2angle(theta5, 'joint5')), 
               self.angle2pwm(self.radius2angle(theta6, 'joint6'))]
        self.all_act(pwm)
        return True

    def all_act(self, pwm):
        #所有舵机同时的速度控制
        ys = []
        step_m = []
        for i in range(len(self.cur_joint_radius)):
            if i != 0:
                ys.append(abs(self.t_pmw[i] - pwm[i]) % self.step_l) #余数
                step_m.append(int(abs(pwm[i] - self.t_pmw[i])/self.step_l))
            elif i == 0:
                ys.append(abs(self.t_pmw[i] - pwm[i]) % self.step_l_0) #余数
                step_m.append(int(abs(pwm[i] - self.t_pmw[i])/self.step_l_0))
        step = 0
        while True:
            self.step_act(self.joint1, step, step_m[0], pwm[0])
            self.step_act(self.joint2, step, step_m[1], pwm[1])
            self.step_act(self.joint3, step, step_m[2], pwm[2])
            self.step_act(self.joint4, step, step_m[3], pwm[3])
            self.step_act(self.joint5, step, step_m[4], pwm[4])
            self.step_act(self.joint6, step, step_m[5], pwm[5])
            step += 1
            if step >= step_m[0] and step >= step_m[1] and step >= step_m[2] and step >= step_m[3] and step >= step_m[4] and step >= step_m[5]:
                break
            time.sleep(self.delay)

        for i in range(len(self.cur_joint_radius)):
            if self.t_pmw[i] < pwm[i]:
                self.t_pmw[i] += ys[i]
                self.action(i, self.t_pmw[i])
            if self.t_pmw[i] > pwm[i]:
                self.t_pmw[i] -= ys[i]
                self.action(i, self.t_pmw[i])

    def action(self, channel, pwm3):
        self.act.setServoPulse(channel, pwm3)

    def s_action(self, channel, pwm4):
        #单一舵机的速度控制
        if not self.t_pmw:
            self.action(channel, pwm4)
            return True
        if channel != 0:
            if self.t_pmw[channel] < pwm4:
                ys = abs(self.t_pmw[channel] - pwm4) % self.step_l #余数
                step_m = int(abs(pwm4 - self.t_pmw[channel])/self.step_l)
                step = 0
                while step < step_m:
                    self.t_pmw[channel] += self.step_l
                    self.action(channel, self.t_pmw[channel])
                    step += 1
                    time.sleep(self.delay)
                self.t_pmw[channel] += ys
                self.action(channel, self.t_pmw[channel])
                return True
            if self.t_pmw[channel] > pwm4:
                ys = abs(self.t_pmw[channel] - pwm4) % self.step_l #余数
                step_m = int(abs(pwm4 - self.t_pmw[channel])/self.step_l)
                step = 0
                while step < step_m:
                    self.t_pmw[channel] -= self.step_l
                    self.action(channel, self.t_pmw[channel])
                    step += 1
                    time.sleep(self.delay)
                self.t_pmw[channel] -= ys
                self.action(channel, self.t_pmw[channel])
                return True
            return False

        elif channel == 0:
            if self.t_pmw[channel] < pwm4:
                ys = abs(self.t_pmw[channel] - pwm4) % self.step_l_0 #余数
                step_m = int(abs(pwm4 - self.t_pmw[channel])/self.step_l_0)
                step = 0
                while step < step_m:
                    self.t_pmw[channel] += self.step_l_0
                    self.action(channel, self.t_pmw[channel])
                    step += 1
                    time.sleep(self.delay)
                self.t_pmw[channel] += ys
                self.action(channel, self.t_pmw[channel])
                return True
            if self.t_pmw[channel] > pwm4:
                ys = abs(self.t_pmw[channel] - pwm4) % self.step_l_0 #余数
                step_m = int(abs(pwm4 - self.t_pmw[channel])/self.step_l_0)
                step = 0
                while step < step_m:
                    self.t_pmw[channel] -= self.step_l_0
                    self.action(channel, self.t_pmw[channel])
                    step += 1
                    time.sleep(self.delay)
                self.t_pmw[channel] -= ys
                self.action(channel, self.t_pmw[channel])
                return True
            return False
        return False  

if __name__ == "__main__":
    a = Cmd()