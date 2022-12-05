"""9. Write a python program to create a School class and 3 instance variables and 1 class
variable."""

class school:
    def __init__(self,human,animal,birds,Tree_name):
        self.human=human
        self.animal=animal
        self.birds=birds
        self.Tree_name=Tree_name


    def Information(school):
        
         if  school.human in ("Rakesh","Aman","Mohit","Subhash","vikas","Felix"):
           print("this is human category :",school.human)
           
         elif school.animal in ("Dog","Cat","Elephant","Goat","Cow"):
             print("this is animal category :",school.animal)
             
         elif school.birds in ("pegion","Peacock","Corw","Parrot"):
             print("this is birdes category :",school.birds) 
             
         else:
             print("this is Tree category :",school.Tree_name)       


sc=school("rakjsdf", "Rabbit", "Gauraiya", "Mango") 
sc.Information()       
        