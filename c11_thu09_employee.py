# GroupName in LEB2: c11_thu09
# FileName: c11_thu09_employee.py
# member list in the file
# 081 Thanakorn Chareonlertkamol
# 095 Bannawit Sanngern
# 129 Napat Adam
# 130 Natthawat Suwansupawong
# deadline thu-31-10-2024 before 14:00

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

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def set_salary(self, new_salary: float) -> None:
        self._salary = new_salary

    def compare(self, another_employee) -> int:
        if self._eid < another_employee.get_eid():
            return -1
        elif self._eid > another_employee.get_eid():
            return 1
        else:
            return 0

    def __repr__(self) -> str:
        return f"Employee(eid: {self._eid}, name: '{self._name}', salary: {self._salary})"

# Sample usage 
# test function
emp1 = Employee(101, "test", 75000)
emp2 = Employee(102, "Bob", 80000)

print(emp1)  # Output: Employee(eid: 101, name: 'Alice', salary: 75000.0)
print(emp1.get_name())  # Output: Alice
emp1.set_name("Alicia")
print(emp1.get_name())  # Output: Alicia
print(emp1.compare(emp2))  # Output: -1 since 101 < 102

# fields: eid: int, name: str, salary: float
# methods: get_eid(), get_name(), get_salary(),
#    set_name(new_name), set_salary(new_salary),
#    constructor(eid, name, salary)
#    representation: Employee(eid: ..., name: ..., salary: ...)
#
# sample code to use the class
#
# special points:
#   method: compare(another_employee)
#      return -1 if this employee.eid < another_employee.eid
#      return 0 if the two employees have the same eid
#      return 1 if this employee.eid > another_employee.eid
