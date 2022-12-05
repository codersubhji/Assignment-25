#5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def cubes_natural(num):
    if num==1:
        return 1
    else:
        return num**3 + cubes_natural(num-1)
    
    
print(cubes_natural(10))    