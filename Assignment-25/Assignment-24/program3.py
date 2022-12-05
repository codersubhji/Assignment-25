"""3. Write a python program to create 2 objects of the user class and assign different
values."""

class user:
    def __init__(self,work,salary):
        self.work=work
        self.salary=salary


use1=user("Engineer", 50000)
use2=user("docter", 40000)
print(use1.work,use1.salary)
print(use2.work,use2.salary)

       