# GroupName in LEB2: c08_thu09
# FileName: c08_thu09_students.py
# member list in the file
# 081 Thanakorn Chareonlertkamol
# 095 Bannawit Sanngern
# 129 Napat Adam
# 130 Natthawat Suwansupawong

def student_data(all: list, id: int, name: str, lastname: str):
    all.append((id, name, lastname))

def validate_id(id: str) -> bool:
    if len(id) != 11:
        return False
    if not id.startswith("67130500"):
        return False
    if not id[8:].isdigit():
        return False
    return True

def read_one_member(all: list):
    while True:
        id = input("Enter student ID (67130500XXX): ")
        if validate_id(id):
            name = input("Enter student first name: ")
            lastname = input("Enter student last name: ")
            student_data(all, id, name, lastname)
            break
        else:
            print("Invalid ID. Please try again.")

def main():
    students = []  
    while True:
        add_student = input("Do you want to add a student member? (yes/no): ").strip().lower()
        if add_student == "yes":
            read_one_member(students)
        elif add_student == "no":
            break
        else:
            print("Please answer 'yes' or 'no'.")
    return students

if __name__ == "__main__":
    students = main()
    print("Students list:", students)