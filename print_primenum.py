#print prime 2-x
def prime(num):
    if num <= 1 :
        return False
    for i in range(2, int(num-1) + 1):
        if num % i == 0:
            return False
    return True

def class_prime(x):
    primes = []
    not_primes = []

    for num in range(2, x+1):
        if prime(num):
            primes.append(num)
        else:
            not_primes.append(num)

    return primes, not_primes
    
x = int(input("enter number: "))
primes, not_primes = class_prime(x)

print(f"Prime numbers from 2 to {x}: {primes}")
print(f"Non-prime numbers from 2 to {x}: {not_primes}")