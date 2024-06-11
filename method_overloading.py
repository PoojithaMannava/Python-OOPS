from multipledispatch import dispatch#pip3 install multipledispatch
@dispatch(int,int)
def addi(a,b):
    print(a+b)
@dispatch(int,int,int)
def addi(a,b,c):
    print(a+b+c)
addi(7,8)
addi(7,8,9)
    
