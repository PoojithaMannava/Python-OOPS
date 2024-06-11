class Parent:
    def pri(self):
        print("I AM PARENT")
class Child(Parent):
    def chi(self):
        print("I AM CHILD")
p1=Parent()
c1=Child()
c1.pri()
c1.chi()
