#9. Write a recursive python function to print octal of a given decimal number

def ocltal_number(num):
    if num==1:
        return num
    elif num==0:
        return num
    else:
       return (num+ocltal_number(num-1))
       
    
    
print(oct(ocltal_number(1))) 
