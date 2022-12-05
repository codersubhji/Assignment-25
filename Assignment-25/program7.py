"""7. Write a python script to create a Phone class with 2 methods to print the features
(calling and sms)."""

class phone:
    def __init__(self,calling,sms,price,color):
        self.calling=calling
        self.sms=sms
        self.price=price
        self.color=color
    
    def first(self):
        return self.calling
    
    def second(self):
        return self.sms    
    
    def third(self):
        return self.price
    
    def fourth(self):
        return self.color

obj=phone("1H:40M:40sec", "hey how are you beb", 500000, "yellow")  

print(obj.first(),obj.second(),obj.third(),obj.fourth(),sep="\n")  