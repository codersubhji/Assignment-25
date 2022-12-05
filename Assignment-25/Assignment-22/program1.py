#1. Write a recursive python function to calculate sum of first N natural numbers

def sumNatural(num):
    if num==1:
        return 1
    else:
        return num+sumNatural(num-1)


print(sumNatural(5))