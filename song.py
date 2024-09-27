n = int(input("Enter a number between 1 and 9: "))

def song(n):
    if not (1 <= n <= 9):
        raise ValueError("Number must be between 1 and 9")
    
    for line in range(1, n + 1):
        print(f"line {line} ", end="")
        for num in range(line, n + 1):
            print(num, end="")
        print()  

song(n)
# Thanakorn Chareonlertkamol 081
# Bannawit Sanngern 095
# Napat Adam 129
# Natthawat Suwansupawong 130