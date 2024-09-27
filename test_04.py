# C4 2024-09-19 THU 11
# Thanakorn Chareonlertkamol 081
# Bannawit Sanngern 095
# Napat Adam 129
# Natthawat Suwansupawong 130
"""write a function to convert kms to miles
- allow only int or float as input parameter
- raise TypeError("Only int or float") if input parameter is a wrong type
- raise ValueError("Only Non-Negative Value") if input parameter is less than 0
- convert km to miles and return float"""

km = 100

def km_to_miles(km):
    if not isinstance(km, (int, float)):
        raise TypeError("Only int or float")
    if km < 0:
        raise ValueError("Only Non-Negative Value")
    miles = km * 5/8
    return float(miles)

print(km_to_miles(km))

"""write a function to check if a string 
has duplicate characters next to each other
- allow only str as input parameter
- raise TypeError if input validation fails
- return bool: True/False
- use while/for loop"""

string = "tt"

def consecutive_char(string):
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            return True
    return False

print(consecutive_char(string))

"""write a function to check if a string 
has duplicate characters
- allow only str as input parameter
- raise ValueError if input validation fails
- return bool: True/False
- use nested while/for loop"""

string = "rtut"

def duplicate(msg: str) -> bool:
    if type(msg) != str:
        raise TypeError
    n = len(msg)
    for i in range(n-1):
        for j in range(i+1, n):
            if msg[i] == msg[j]:
                return True
    return False

print(duplicate(string))

"""write a function to find the maximum value of the three int parameters
- allow only int as input parameter
- raise TypeError if input validation fails
- return the maximum value of the three values
- use only comparison: <, >, <=, >=, !=, ==
- not allow the use of lists or any function
- multiple parameters with the same value has no effect to the return value"""
x = 3
y = 1
z = 99

def max_value(x: int, y: int, z: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        raise TypeError("All inputs must be integers")
    if x >= y:
        if x >= z:
            return x
        return z
    else:
        if y >= z:
            return y
        return z
print(max_value(x, y, z))