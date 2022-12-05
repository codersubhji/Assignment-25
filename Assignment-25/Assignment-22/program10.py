#10. Write a recursive python function to find the Nth term of the Fibonacci series.

def fabonacci_series(num):
    if num==0 or num==1:
        return 1
    else:
        return (fabonacci_series(num-1) + fabonacci_series(num-2))
      

print(fabonacci_series(5))   
        