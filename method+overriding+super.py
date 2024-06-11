class Parent:
    def pp(self):
        print("i am parent")
class Ch(Parent):
    def pp(self):
        super().pp() #super keyword
c=Ch()
c.pp()

        
