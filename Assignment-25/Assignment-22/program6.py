#6. Write a recursive python function to calculate the factorial of a number.

def fact_natural(num):
    if num==1:
        return 1
    else:
        return num * fact_natural(num-1)
    
    
    
print(fact_natural(5))    
