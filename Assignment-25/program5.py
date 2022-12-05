"""5. Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values."""

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def sum1(self):
        print("sum of two number is :",self.num1+self.num2)
        
    def sub1(self):
        print("sum of two number is :",self.num1-self.num2)
        
    
      
        
obj=calculator(5, 3)
obj.sum1()
obj.sub1()
             
        
            