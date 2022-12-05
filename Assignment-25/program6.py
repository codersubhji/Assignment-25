"""6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class."""

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def sum1(self):
        print("sum of two number is :",self.num1+self.num2)
        
    def sub1(self):
        print("sum of two number is :",self.num1-self.num2)
class calculator2_0(calculator):
    def mul(self):
        print("multiple of two number is :",self.num1*self.num2)
                
    def dev(self):
        print("devision of two number is :",self.num1/self.num2)
        
obj = calculator2_0(10, 5)
obj.sum1()
obj.sub1()
obj.mul()
obj.dev()         