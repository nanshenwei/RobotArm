import tornado.ioloop
import tornado.web
import command

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument("password") == "12345":
            self.write({"errcode":1})
        else:
            self.write({"errcode":0})

class ControlHandler(tornado.web.RequestHandler):
    Cmd = command.Cmd()
    def angel2servoAngel(self,joint,angel):
        if joint == 1:
            return angel + 135
        if joint == 2:
            return angel + 180
        if joint == 3:
            return angel
        if joint == 4:
            return angel + 120
        if joint == 5 or joint == 6:
            return angel + 90

    def get(self):
        joint = int(self.get_argument("joint"))
        angel = int(self.get_argument("angel"))
        if joint == 1:
            pwm = self.Cmd.angle2pwm(self.angel2servoAngel(joint,angel), 270)
        else:
            pwm = self.Cmd.angle2pwm(self.angel2servoAngel(joint,angel))
        if self.Cmd.s_action(joint-1, pwm):
            self.write({"errcode":1,
                        "angel":angel})
        

app = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/control", ControlHandler)
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()