# 1. Write a function "f1()" that receives two numbers and returns true
# if the first number less than the second number, otherwise return false.

def f1(a, b):
    return a < b
print(f1(3, 5))  # True
print(f1(5, 3))  # False

# 2. Write a function "f2()" that takes an integer (x) and returns a list containing all integers from 0 to x.
# Note that x can be positive, negative, and zero.

def f2(x):
    result = []
    i = 0
    if x >= 0:
        while i <= x:
            result.append(i)
            i += 1
    else:
        while i >= x:
            result.append(i)
            i -= 1
    return result

print(f2(5))
print(f2(-3))
print(f2(0))

# 3. Write a function "f3()" that receives a list and returns (counts) the number of items in the list
# that has the smallest value.

def f3(list):
    if not list:
        return 0
    min_value = min(list)
    count = 0
    i = 0
    while i < len(list):
        if list[i] == min_value:
            count += 1
        i += 1
    return count

print(f3([5, 7, 3, 7, 5, -3, -8, 4, -8, 5, 7]))  # 2

# 4. Write a function "f4()" that receives a list (x) and a boolean function (f).  
# The function "f4()" returns (counts) the number of items in the list where f(x[i]) returns True.

def f4(list, f):
    count = 0
    i = 0
    while i < len(list):
        if f(list[i]):
            count += 1
        i += 1
    return count

is_even = lambda x: x % 2 == 0
print(f4([1, 2, 3, 4, 5, 6], is_even))  # 3

# 5. Write a function "f5()" that receives a list and returns the second-smallest value.
# If there is no item or only one item in the list or all items in the list have the same value,
# this function returns None. (Try not to use sorting or set/dict data structures).

def f5(lst):
    if len(lst) < 2:
        return None

    first_min = float('inf')
    second_min = float('inf')
    has_second_min = False

    i = 0
    while i < len(lst):
        num = lst[i]
        if num < first_min:
            second_min = first_min
            first_min = num
            has_second_min = True
        elif first_min < num < second_min:
            second_min = num
            has_second_min = True
        i += 1

    return second_min if has_second_min else None

print(f5([5, 3, 9, 3, 7, 5]))  # 5
print(f5([5, 5, 5]))           # None