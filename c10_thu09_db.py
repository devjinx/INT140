# GroupName in LEB2: c10_thu09
# FileName: c10_thu09_db.py
# member list in the file
# 081 Thanakorn Chareonlertkamol
# 095 Bannawit Sanngern
# 129 Napat Adam
# 130 Natthawat Suwansupawong

def main():
    list_of_dicts = []  # list of dict {"id": ..., "name": ..., "lastname": ...}
    dict_of_lists = {"ids": [], "names": [], "lastnames": []}  # dict of 3 lists
    
    # Continue running until explicitly asked to exit
    while True:
        # Decomposition: separate input and action logic
        action = input("Choose an action: add/find/exit: ").strip().lower()

        # Pattern recognition: handling common actions with clear flow
        if action == "exit":
            break  # Exit the program
        
        elif action == "add":
            # Collecting and processing student information
            id, name, lastname = read_one_student()

            # Abstraction: focusing on unique ID validation
            if not is_unique_id(list_of_dicts, id):
                print(f"Error: ID {id} is already in use.")
                continue  # Skip adding this student if ID is not unique

            # Algorithm design: separate functions for adding data
            add_student_to_dict(list_of_dicts, id, name, lastname)
            add_student_to_lists(dict_of_lists, id, name, lastname)
            print(f"Student {name} {lastname} added successfully.")

        elif action == "find":
            # Decomposition: Ensure ID format is correct before searching
            id_to_find = validate_student_id()
            find_student_by_id(list_of_dicts, id_to_find)

        else:
            print("Invalid action. Please choose 'add', 'find', or 'exit'.")

    print("Program exited.")

def read_one_student() -> (int, str, str):
    """Ask the user to input student details, validate ID, and ensure name and lastname are not empty."""
    # Decomposition: Loop until valid ID format is provided
    while True:
        id = input("Enter student ID (67130500XXX): ").strip()
        if len(id) == 11 and id.startswith("67130500") and id[8:].isdigit():
            id = int(id)
            break
        print("Invalid ID. It must be in the format 67130500XXX where X is a digit.")
    
    # Decomposition: Ensure name is not empty
    while True:
        name = input("Enter student first name: ").strip()
        if name:
            break
        print("First name cannot be empty. Please enter a valid first name.")
    
    # Decomposition: Ensure lastname is not empty
    while True:
        lastname = input("Enter student last name: ").strip()
        if lastname:
            break
        print("Last name cannot be empty. Please enter a valid last name.")
    
    return id, name, lastname

def validate_student_id() -> int:
    """Ensure the student ID is valid and follows the correct format."""
    while True:
        id_to_find = input("Enter student ID to find (67130500XXX): ").strip()
        if len(id_to_find) == 11 and id_to_find.startswith("67130500") and id_to_find[8:].isdigit():
            return int(id_to_find)
        print("Invalid ID format. Please enter a valid ID in the format 67130500XXX.")

def is_unique_id(students: list, id: int) -> bool:
    """Decomposed: Check if ID is unique."""
    for student in students:
        if student['id'] == id:
            return False
    return True

def add_student_to_dict(students: list, id: int, name: str, lastname: str):
    """Decomposed: Add student details to the list of dictionaries."""
    student_dict = {"id": id, "name": name, "lastname": lastname}
    students.append(student_dict)

def add_student_to_lists(students: dict, id: int, name: str, lastname: str):
    """Decomposed: Add student details to the dictionary of lists."""
    students["ids"].append(id)
    students["names"].append(name)
    students["lastnames"].append(lastname)

def find_student_by_id(students: list, id: int):
    """Decomposed: Search for student by ID in the list of dictionaries."""
    for student in students:
        if student['id'] == id:
            print(f"Student found - ID: {student['id']}, Name: {student['name']}, Lastname: {student['lastname']}")
            return
    print(f"Student with ID {id} not found.")

if __name__ == "__main__":
    main()