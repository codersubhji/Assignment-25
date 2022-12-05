"""4. Write a recursive python function to calculate sum of squares of first N natural
numbers"""

def sum_square_natural(num):
    if num==1:
        return 1
    else:
        return num*num + sum_square_natural(num-1)
    
    
print(sum_square_natural(5))   


#or

#        if num>0:
#            sr=num*num
#            return sr+sum_square_natural(num-1)
#        else:
#            return 0

# print(sum_square_natural(5))       



 
        