#2. Write a python script to update the above Profile class with encapsulation.

class profile:
    def __init__(self,price,color, name):
        self.price=price
        self.color=color
        self.name=name
      # or using set and get method we are trying to update class profile 
      #we are also update without using any set or get method  
    def set_profile(self,new_value):
        self.price=new_value
        
    def get_profile(self):
        return self.price       


obj=profile(50000, "Blue", "Fortuner") 
 
obj.set_profile(180000)
obj.get_profile()

# or these term using without set or get method
# obj.price=300000 

print(obj.price,obj.color,obj.name)     
        
        
        