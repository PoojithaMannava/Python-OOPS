class gp:
    def gpp(self):
        print("i am gp")
class p:
    def pp(self):
        print("i am parent")
class c(p,gp):
    def c(self):
        print("i am child")
c1=c()
c1.gpp()
c1.pp()
