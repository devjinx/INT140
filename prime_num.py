def prime(num):
    if num <= 1 :
        return False
    for i in range(2, int(num-1) + 1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter number:"))

if prime(num):
     print("prime")
else:
     print("not prime")