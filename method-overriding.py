class Parent:
    def pp(self):
        print("i am parent class")
class ch(Parent):
    def pp(self):
        print("i am child class")
c=ch()
c.pp()
