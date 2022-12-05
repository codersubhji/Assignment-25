"""8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size."""


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


lp1=Laptop("Acer", 32, "Ryzon9", "10TB") 
lp2=Laptop("hp", 5, "Core9", "5TB") 
lp3=Laptop("Acer", 8, "i9", "1TB") 


l1=[]
for i in (lp1.ram,lp2.ram,lp3.ram):
    l1.append(i)
x=sorted(l1)    
print("in sorted oreder of ram ..:",x)        