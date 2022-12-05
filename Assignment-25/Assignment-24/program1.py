#1. Write a python program to create a user class with 3 properties : name, age, email.

class personal:
    def __init__(self,name,gender,age,email):
        self.name=name
        self.gender=gender
        self.age= age
        self.email=email
        
     # according to question we are just use of three properties
     
per=personal("Subh Ji","Male",21,"subhji74@gmail.com")
print(per.name,per.gender ,per.age,per.email ,sep="\n ")   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 # this is advance things       

# def customer(personal):
#     if personal.gender=="Male":
#         print("Hello ",personal.name,"sir")
        
#     else:
#         print("Hello ",personal.name,"ma'am") 
                   
# def details(personal):
#     print("Your age is ",personal.age)
#     print("your email is ",personal.email)  
    
    
          
# cust=personal("Sruti","Femail",34,"subhji7383@gmail.com")    
# customer(cust)  
# details(cust)
  



        

    