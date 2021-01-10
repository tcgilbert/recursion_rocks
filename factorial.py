# You will have to figure out what parameters to include
#  All functions must use recursion 

# This function returns the factorial of a given number.

def factorial(n):
    print(n)
    if (n == 1):
        result = 1
    else:    
        result = n * factorial(n - 1)
    return result

print(factorial(5))
# => 120