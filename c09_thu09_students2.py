# GroupName in LEB2: c09_thu09
# FileName: c09_thu09_students2.py
# member list in the file
# 081 Thanakorn Chareonlertkamol
# 095 Bannawit Sanngern
# 129 Napat Adam
# 130 Natthawat Suwansupawong

def main():
    list_of_dicts = []  # list of dict {"id": ..., "name": ..., "lastname": ...}
    dict_of_lists = {"ids": [], "names": [], "lastnames": []}  # dict of 3 lists
    
    while True:
        # Ask if user wants to add a student
        add_more = input("Do you want to add a student? (yes/no): ").strip().lower()
        if add_more == "no":
            break

        # Collect student info
        id, name, lastname = read_one_student()

        # Check if the ID is unique
        if not is_unique_id(list_of_dicts, id):
            print(f"Error: ID {id} is already in use.")
            continue  # Skip adding this student if ID is not unique

        # Add the student to the list of dicts and the dict of lists
        add_student_to_dict(list_of_dicts, id, name, lastname)
        add_student_to_lists(dict_of_lists, id, name, lastname)

    # Print the results
    print("\nStudents from dict:")
    print_students_from_dict(list_of_dicts)
    
    print("\nStudents from lists:")
    print_students_from_list(dict_of_lists)


def read_one_student() -> (int, str, str):
    """Ask the user to input student details and validate ID format."""
    while True:
        id = input("Enter student ID (67130500XXX): ").strip()
        if len(id) == 11 and id.startswith("67130500") and id[8:].isdigit():
            id = int(id)
            break
        print("Invalid ID. It must be in the format 67130500XXX where X is a digit.")
    
    name = input("Enter student first name: ").strip()
    lastname = input("Enter student last name: ").strip()
    
    return id, name, lastname


def is_unique_id(students: list, id: int) -> bool:
    """Helper function to check if the ID is unique in list_of_dicts."""
    for student in students:
        if student['id'] == id:
            return False
    return True


def add_student_to_dict(students: list, id: int, name: str, lastname: str):
    """Add a student as a dictionary entry to the list."""
    student_dict = {"id": id, "name": name, "lastname": lastname}
    students.append(student_dict)


def add_student_to_lists(students: dict, id: int, name: str, lastname: str):
    """Add a student’s details to the respective lists."""
    students["ids"].append(id)
    students["names"].append(name)
    students["lastnames"].append(lastname)


def print_students_from_dict(students):
    """Print each student from the list of dictionaries."""
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Lastname: {student['lastname']}")


def print_students_from_list(students):
    """Print each student from the dict of lists."""
    for i in range(len(students["ids"])):
        print(f"ID: {students['ids'][i]}, Name: {students['names'][i]}, Lastname: {students['lastnames'][i]}")


if __name__ == "__main__":
    main()