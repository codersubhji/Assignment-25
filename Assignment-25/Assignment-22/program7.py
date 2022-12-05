#7. Write a recursive python function to calculate sum of the digits of a given number

def sum_digit_Number(num):
    if num==0:
        return 0
    else:
        return ((num%10) + sum_digit_Number(num//10))
  
print(sum_digit_Number(123))     
