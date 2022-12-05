"""3. Write a python script to update 2nd Question, change email and age to __email and
__age."""

class profile:
    def __init__(self,email,age):
        self.__email=email
        self.__age=age

    def set_email(self,new_email):
        self.__email=new_email
    def get_email(self):
        return self.__email
    def set_age(self,new_age):
        self.__age=new_age
    def get_age(self):
        return self.__age        

obj=profile("subjidslf", 20) 

obj.set_email("rahulsingh94408@gmail.com")

obj.set_age(30)

print(obj.get_email(),obj.get_age())      