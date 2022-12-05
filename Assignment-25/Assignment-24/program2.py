#2. Write a python program to create a user class with a method to greet the user.

class User:
    def __init__(self,name,look):
        
        self.name=name
        self.look=look
def greet(User) :
    if User.look in ("beautiful","Charming","prety","cute"):
        print("Hello",User.name,"Ma'am , You are",User.look )
    else:
        print("Hello",User.name,"Sir , You are",User.look)  


us=User("Anjali", "beautiful")  
greet(us)              