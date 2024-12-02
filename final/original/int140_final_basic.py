"""
INT140 Problem and Solution for Final Exam Preparation
"""

from functools import reduce

""" ===============================================================
Problem_01: Write a function 'func01' that receives two numbers.
This function returns true if the first number is less than the second number,
otherwise it returns false. This function does not validate its parameters.
e.g., 
func01(10.1, 9.9) -> False
func01(5, 5.3) -> True
"""
# def func01(num1: int|float, num2: int|float) -> bool:  ## with type hint
def func01(num1, num2):  ## without type hint
    return num1 < num2

""" ===============================================================
Problem_02: Write a function 'func02' that receives two strings. 
This function returns true if the first string is a part of the second string, 
otherwise return false. This function does not validate its parameters.
e.g., 
func02('over', 'forever') -> False
func02('lie', 'believe') -> True
"""
# def func02(str1: str, str2: str) -> bool:  ## with type hint
def func02(str1, str2):  ## without type hint
    return str1 in str2

""" ===============================================================
Problem_03: Write a function 'func03' that receives two numbers
which are the lengths of the two sides of the right angle of a right triangle.
(ฟังก์ชันนี้ รับพารามิเตอร์เป็นตัวเลขสองตัว ที่เป็นความยาวของ สองด้านที่ประกอบมุมฉาก ของสามเหลี่ยมมุมฉาก)
This function returns the length of the side opposite to the right angle.
This function must validate that the two parameters are positive numbers.
It raises ValueError if any of two parameters is not a positive number.
e.g.,
func03(4, 3) -> 5.0
func03(5, 12.0) -> 13.0
func03(-3.0, 4) -> ValueError
"""
# def func03(side1:int|float, side2:int|float) -> float:  ## with type hint
def func03(side1, side2):  ## without type hint
    if side1 <= 0 or side2 <= 0:
        raise ValueError("at least one of the two parameters is not a positive number.")
    return (side1 ** 2 + side2 ** 2) ** 0.5

""" ===============================================================
Problem_04: Write a function 'func04' that receives a list of integers.
This function counts the number of even numbers in the list.
(ฟังก์ชันนี้ นับจำนวนเลขคู่ ที่มีอยู่ในลิสต์)
Even numbers are the number that is divisible by 2. (even_number % 2 == 0)
This function does not validate its parameter.
e.g., 
func04([3, -2, 7, 0, 12, 6, -9]) -> 4
"""
# def func04(ls: list[int]) -> int:  ## with type hint
def func04(ls):  ## without type hint
    counter = 0
    for n in ls:
        if n % 2 == 0:
            counter += 1
    return counter

""" ===============================================================
Problem_05: Write a function 'func05' that receives a list of values 
(the first parameter) and a value (the second parameter).
This function counts the number of values in the list (the first parameter) 
that is less than the value (the second parameter).
(ฟังก์ชันนี้ นับจำนวนค่าในลิสต์ ที่มีค่าน้อยกว่าค่าของพารามิเตอร์ตัวที่สอง)
This function does not validate its parameters.
The values in the list and the value of the second parameters may be 
integers, floats, strings, or any type that can be compared using < (less than).
e.g.,
func05([], 10) -> 0
func05(['hate', 'love', 'angry', 'fun', 'hunger'], 'happy') -> 2
func05([6, -12.5, 71, 4, 10], 9.9) -> 3
"""
# def func05(ls: list, value) -> int:  ## with type hint
def func05(ls, value):  ## without type hint
    counter = 0
    for n in ls:
        if n < value:
            counter += 1
    return counter

""" ===============================================================
Problem_06: Write a function 'func06' that receives an integer
and returns a list containing all integers starting from 0 to that integer.
The parameter can be positive, negative, and zero.
This function does not validate its parameter.
You must use a loop to append each element into the list.
e.g.,
func06(0) -> [0]
func06(4) -> [0, 1, 2, 3, 4]
func06(-3) -> [0, -1, -2, -3]
"""
# def func06(num: int) -> list[int]:  ## with type hint
def func06(num):  ## without type hint
    step = 1         # each step will increase by 1
    if num < 0:      # but if the parameter is negative
        step = -1    #    each step will decrease by 1 instead
    value = 0                   # start the value from 0
    result = [value]            # start the result with [value]
    while value != num:         # loop until the value equals to the parameter
        value += step           # move one step closer to the parameter
        result.append(value)    # append the value to the result
    return result

""" ===============================================================
Problem_07: Write a function 'func07' that receives a list of strings
and returns the summation of the length of all strings in the list.
This function does not validate its parameter.
e.g., 
func07(['one', 'two', 'three', 'four', 'five']) -> 19
"""
# def func07(ls: list[str]) -> int:  ## with type hint
def func07(ls):  ## without type hint
    result = 0
    for i in ls:
        result += len(i)
    return result

""" ===============================================================
Problem_08: Write a function 'func08' that receives a list of strings
and returns a string concatenating the first letter of each string in the list.
An empty string is returned if the list is empty or the list contains only empty strings.
This function does not validate its parameter.
e.g., 
func08(['Strength', 'Weakness', 'Opportunity', 'Threat']) -> 'SWOT'
"""
# def func08(ls: list[str]) -> str:  ## with type hint
def func08(ls):  ## without type hint
    result = ""
    for i in ls:
        if len(i) > 0:
            result += i[0]
    return result

""" ===============================================================
Problem_09: Write a function 'func09' that receives a list containing values.
The values may be int, float, str, or any type that can be compare with < and ==. 
This function counts the number of values in the list that are equal to 
the smallest value in the list.  This function returns the count.
(ฟังก์ชันนี้ นับจำนวน ของค่าในลิสต์ ที่มีค่าเท่ากับ ค่าที่ต่ำที่สุดในลิสต์)
For example, if the list is [5, -3, 7, 6, -3, 5, -1, 5], the result is 2
because the smallest value in the list is -3 and there are 2 values in the list equals to -3.
If the list is ['is', 'am', 'are', 'do', 'am', 'is', 'have', 'am', 'are'], the result is 3
because the smallest value is 'am' and there are 3 'am' in the list.
If the list is an empty list (containing no values), then there is no smallest value, 
it returns 0.  This function does not validate its parameter.
"""
def func09(ls):  ## without type hint
    if len(ls) == 0:
        return 0
    counter = 0  # for counting the number of elements equal to minimum value
    min_value = ls[0]  # let element_0 be the minimum
    for value in ls:
        if value < min_value:     # if found a new minimum
            min_value = value     #    remember the new minimum
            counter = 1           #    restart the counter to 1
        elif value == min_value:  # elif found the old minimum
            counter += 1          #    increment the counter
    return counter

""" ===============================================================
Problem_10: Write a function 'func11' that receives a list containing values 
(which may be int, float, str, or any value that can be compared with == and <).
This function returns the second-smallest value in the list.  This function returns None 
if there is less than 2 values in the list or all values in the list are all equal.
Do not to use sorting techniques or duplicate removal techniques (e.g. set/dict).
This function does not validate its parameter.
e.g.,
func10([]) -> None
func10(['x']) -> None
func10(['a', 'a']) -> None
func10(['a', 'b']) -> 'b'
func10(['b', 'a']) -> 'b'
func10([300, -11, -20, -11, 300, -20, 50000, 300, 4000]) -> -11
"""
def func10(ls):  ## without type hint
    size = len(ls)
    if size < 2:
        return None
    smallest = ls[0]  # let element_0 be the smallest
    second = None     # let the second smallest be unassigned
    for v in ls:                # loop through all elements in the list
        if v < smallest:        #    if found the new smallest value
            second = smallest   #       move the old smallest value to be the second-smallest value
            smallest = v        #       and set the new smallest value
        elif smallest < v and (second is None or v < second):
                                #    elif found the new second-smallest value
            second = v          #       set the new second-smallest value
    return second
