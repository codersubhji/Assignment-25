"""10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values"""

class employee:
    def __init__(self,empid,name,salary):
        self.empid=0
        self.name=''
        self.salary=0
    
    def show_let_by_users(employee):
        
        employee.empid=int(input("enter any I'd of employee :"))
        employee.name=input("Enter any name of employee :")    
        employee.salary=int(input("enter salary of a midlevel employee :"))
        
        
        print(employee.empid)
        print(employee.name)
        print(employee.salary)
        

emp=employee(0,"",0)
print(emp.show_let_by_users())      
        