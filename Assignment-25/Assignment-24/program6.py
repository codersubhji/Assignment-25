#6. Write a python program to create 3 user objects and find the youngest of all.


class user:
    
    def __init__(self,young):

        self.young=young


y1=user(20)
y2=user(15)
y3=user(40)

if y1.young>y2.young and y1.young>y3.young:
    print("youngest person which age is ",y1.young ,"year")
elif y2.young>y3.young  and y2.young>y1.young:
    print("youngest person which age is ",y2.young ,"year")     
else:
    print("youngest person which age is ",y3.young ,"year")         