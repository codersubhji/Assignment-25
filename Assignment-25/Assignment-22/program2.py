#2. Write a recursive python function to calculate sum of first N odd natural numbers

def sum_of_odd(num):
   if num>0:
     odd1=(num*2)-1
     return odd1+sum_of_odd(num-1)
   else:
     return 0
print(sum_of_odd(0))


    
        