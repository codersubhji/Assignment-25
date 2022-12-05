"""7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values)."""

class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    def brand_show(self):
        print("Brand name of Laptop is :",self.brand)
        print("How much ram in this laptop :",self.ram)
    
    def about_laptop(self):
        print("cpu name is :",self.cpu)
        print("how many hard disk in your laptop:",self.hdd) 


lp=Laptop("Acer", "32 GB", "Ryzon9", "5 TB")      
lp.brand_show()
lp.about_laptop()    
        
    
    

            
        