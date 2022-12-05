"""4. Write a python script to update 2nd Question, add a class variable (platform) and
create a classmethod to access it."""

class profile:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
class plateform(profile):
    
    def class_method(self):
        return self.name,self.age
        
obj=plateform("Subhash", 20)  
print(obj.name,obj.age)    
            


