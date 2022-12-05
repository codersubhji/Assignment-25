#8. Write a recursive python function to print binary of a given decimal number.

def binary(num):
    if num==1:
        return num
    elif num==0:
        return num
    else:
       return (num+binary(num-1))
       
    
    
print(bin(binary(1)))    
# a,b= 10,20
# c=a+b
# print(bin(c))