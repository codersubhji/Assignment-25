#3. Write a recursive python function to calculate sum of first N even natural numbers

def sum_N_even(num):
    if num>0:
        evn=(num*2)
        return evn + sum_N_even(num-1)
    else:
        return 0
print(sum_N_even(5))    