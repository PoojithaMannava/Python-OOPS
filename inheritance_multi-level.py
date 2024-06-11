class Gp:
    def gp(self):
        print("I am Gp")
class Pa(Gp):
    def pa(self):
        print("I am pa")
class Ch(Pa):
    def ch(self):
        print("I am child")

c1=Ch()
c1.gp()
c1.pa()
c1.ch()
