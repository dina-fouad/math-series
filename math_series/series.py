def fibonacci(n):

        if n == 0:
            return 0
        if n==1:
            return 1
    
        return fibonacci(n-1) + fibonacci(n-2) 
#print(fibonacci(7))


def lucas(n):

        if n == 0:
            return 2
        if n==1:
            return 1
    
        return lucas(n-1) + lucas(n-2) 
#print(lucas(3))


def sum_series(n,f=0,s=1):
    
    if n==0:
        return f
    if n==1:
        return s
   
    return sum_series(n-1,f,s)+sum_series(n-2,f,s)
print(sum_series(7,f=0,s=1))    


       

        