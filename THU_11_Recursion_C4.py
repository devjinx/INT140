#   
# 081 Thanakorn Chareonlertkamol
# 095 Bannawit Sanngern
# 129 Napat Adam
# 130 Natthawat Suwansupawong

# base case, recursive case

# n : positive integer
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)! ; 0! = 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
number = 5  
result = factorial(number)
print(f"The factorial of {number} is {result}")

# x : non-zero number
# n : positive integer
# x^n = x * x * x * ... * x (n numbers of x)
# x^n = x * x^(n-1) ; x^0 = 1
def exponential(x, n):
    if n == 0:
        return 1
    else:
        return x * exponential(x, n-1)

base = 2  
exponent = 3  
result = exponential(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")

# n : positive integer
# f(n) = f(n-1) + f(n-2) ; f(1) = 0, f(2) = 1
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
position = 6  
result = fibonacci(position)
print(f"The Fibonacci number at position {position} is {result}")

# s : character strings, e.g. 'eve', 'madam', 'anywhere'
# palindrome returns True if backward sequence == forward sequence
#            otherwise return False
def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

s = 'anything'
print(len(s)) # length of the string: 8
print(s[0]) # 'a'
print(s[len(s)-1]) # 'g'
print(s[7]) # 'g'