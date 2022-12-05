"""8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class."""


class phone:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def sum1(self):
        print("sum of two number is :",self.num1+self.num2)
        
    def sub1(self):
        print("sum of two number is :",self.num1-self.num2)
class calculator2_0(phone):
    def mul(self):
        print("multiple of two number is :",self.num1*self.num2)
                
    def dev(self):
        print("devision of two number is :",self.num1/self.num2)
        
        
class smartphone(calculator2_0):  
    
    def modulo(self):
        print("modulous of two number is :",self.num1%self.num2)
    
    def integer(self):
        print("find the enteger vlaue after devided of two nubmer is :",self.num1//self.num2)         
        
obj=smartphone(20, 3)
obj.sum1()
obj.sub1()
obj.mul()
obj.dev()
obj.modulo()
obj.integer()      