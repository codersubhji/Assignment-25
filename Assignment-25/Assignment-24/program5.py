#5. Write a python program to delete the age property of the user.

class user:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def my_fun(user):
        print("My name is ",user.name)
        print("I 'm ",user.gender)
            
p1=user("Subhash", 20, "Male")        
print(p1.my_fun())
del p1.age

print(p1.age)


