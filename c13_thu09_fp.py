# group id (in LEB2): c13_thu09
# filename: c13_thu09_fp.py
# 081 Thanakorn Chareonlertkamol
# 095 Bannawit Sanngern
# 129 Napat Adam
# 130 Natthawat Suwansupawong
#submission deadline: Sun 17 Nov 2024 before midnight (23:59)

"""

1. create a class named Employee with the following fields:
_eid, _name, _salary
with a constructor (__init__), all getter/setter methods
and __str__ method

2. create a list of at list 6 employees

3. create the following functions to
3.1 filter a list of Employees who has salary > 1000
3.2 map a list of Employees to a list of Employee's name
3.3 compute an average salary of all Employees on a list
*** 
a) write 3.1-3.3 using functional programming style
b) generalize 3.1-3.3 so that the functions can receive
other functions for filtering, mapping, or reduction

"""

from typing import Callable, List
from functools import reduce

class Employee:
    def __init__(self, eid: int, name: str, salary: float):
        self._eid = eid
        self._name = name
        self._salary = salary

    def get_eid(self) -> int:
        return self._eid

    def get_name(self) -> str:
        return self._name

    def get_salary(self) -> float:
        return self._salary

    def set_eid(self, eid: int):
        self._eid = eid

    def set_name(self, name: str):
        self._name = name

    def set_salary(self, salary: float):
        self._salary = salary

    def __str__(self) -> str:
        return f"Employee(eid={self._eid}, name={self._name}, salary={self._salary})"


# Sample list of employees
employees = [
    Employee(1, "Alice", 1200),
    Employee(2, "Bob", 800),
    Employee(3, "Charlie", 1500),
    Employee(4, "Diana", 900),
    Employee(5, "Eve", 1100),
    Employee(6, "Frank", 1000)
]

# Functional approach with higher-order functions
def filter_employees(employees: List[Employee], predicate: Callable[[Employee], bool]) -> List[Employee]:
    return list(filter(predicate, employees))

def map_employees(employees: List[Employee], mapper: Callable[[Employee], any]) -> List[any]:
    return list(map(mapper, employees))

def reduce_employees(employees: List[Employee], reducer: Callable[[float, float], float], initial: float) -> float:
    return reduce(reducer, map(lambda emp: emp.get_salary(), employees), initial)

# Specific functions based on general higher-order functions
filtered_employees = filter_employees(employees, lambda emp: emp.get_salary() > 1000)
mapped_names = map_employees(employees, lambda emp: emp.get_name())
average_salary = reduce_employees(employees, lambda acc, salary: acc + salary, 0) / len(employees)

# Output
print("Employees with salary > 1000:", [str(emp) for emp in filtered_employees])
print("Employee names:", mapped_names)
print("Average salary:", average_salary)