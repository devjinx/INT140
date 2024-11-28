# 1. write a function "f1()" that receives two numbers and returns true
# if the first number less than the second number, otherwise return false.

def f1(a,b):
    return a < b
print(f1(3,5)) #True
print(f1(5,3)) #False

# 2. write a function "f2()" that an integer (x) and returns a list containing all integers from 0 to x.
# note that x can be positive, negative, and zero.

def f2(x):
    if x >= 0:
        return list(range(0,x+1))
    else:
        return list(range(0,x-1,-1))
print(f2(5))
print(f2(-3))
print(f2(0))

# 3. write a function "f3()" that receives a list and returns (counts) the number of items in the list
# that has the smallest value. e.g., if input is [5, 7, 3, 7, 5,-3, -8, 4, -8, 5, 7], the result is 2
# because -8 is the smallest value and there are 2 items have value = -8.

def f3(lst):
    if not lst: 
        return 0
    min_value = min(lst)
    return lst.count(min_value)
print(f3([5, 7, 3, 7, 5, -3, -8, 4, -8, 5, 7]))  # 2

# 4. write a function "f4()" that receives a list (x) and a boolean function (f).  
# function f4() returns (counts) the number of items in the list that f(x[i]) returns True.
# the boolean function (f) is a function that receives a value and returns a boolean value (true or false).

def f4(list, f):
    return sum(1 for item in list if f(item))
is_even = lambda x: x % 2 == 0
print(f4([1, 2, 3, 4, 5, 6], is_even))  # 3

# 5. write a function "f5()" that recieves a list and the second-smallest value.
# If there is no item or only one item in the list or all items in the list have the same value,
# this function returns None. (try not to use sorting or set/dict data structures)
def f5(lst):
    if len(lst) < 2:
        return None

    first_min = float('inf')
    second_min = float('inf')
    has_second_min = False

    for num in lst:
        if num < first_min:
            second_min = first_min
            first_min = num
            has_second_min = True
        elif first_min < num < second_min:
            second_min = num
            has_second_min = True

    return second_min if has_second_min else None
print(f5([5, 3, 9, 3, 7, 5]))  # 5
print(f5([5, 5, 5]))           # None