def a(x, q):
    if q:
        print('yyyyyyy')
    print(x+q)

def b():
    v = [12,
         23,
         123]
    return v


a(b()[0]+1, 3)
for i in range(4):
    print(i)

print(i)
print(int(34.2))
print(int(25.9))


class Cmd:
    cmd1=1
    def __init__(self):
        self.cmd1=2
        print(self.cmd1)
    def p(self):
        print(self.cmd1)
        
amd = Cmd()
amd.cmd1 = 3
amd.p()
import math

print(math.radians(180))
