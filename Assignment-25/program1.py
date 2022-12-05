#1. Write a python script to create a Profile class with 3 attributes (name, email, age).

class profile:
    def __init__(self,name,email,age):
        
        print("Inside the constructor..")
        self.name=name
        self.email=email
        self.age=age

class details(profile):
    pass 

obj=profile("Rahul", "rahul7788@gmail.com", 40)   
print(obj.name,obj.email,obj.age)    