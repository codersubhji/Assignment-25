#4. Write a python program to init default values for user object using __init__ method.

class user:
    def __init__(self,name , mobile_number):
        self.name=name
        self.mobile_number=mobile_number
    def details(user):
        print(user.name," ",user.mobile_number)  



sb=user("subhash", 6393764098)  
sb.details()        