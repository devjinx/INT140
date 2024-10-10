from c09_thu09_students2 import *


def test():
    """Test cases for the main functionality."""
    list_of_dicts = []  # list of dict {"id": ..., "name": ..., "lastname": ...}
    dict_of_lists = {"ids": [], "names": [], "lastnames": []}  # dict of 3 lists

    # Simulated input data
    students_to_add = [
        (67130500123, "John", "Doe"),
        (67130500124, "Jane", "Smith"),
        (67130500123, "Alice", "Brown")  # Duplicate ID
    ]
    
    # Simulate adding students
    for student in students_to_add:
        id, name, lastname = student
        if not is_unique_id(list_of_dicts, id):
            print(f"Error: ID {id} is already in use.")
            continue
        add_student_to_dict(list_of_dicts, id, name, lastname)
        add_student_to_lists(dict_of_lists, id, name, lastname)

    # Print results for validation
    print("\nStudents from dict:")
    print_students_from_dict(list_of_dicts)
    
    print("\nStudents from lists:")
    print_students_from_list(dict_of_lists)

    # Assertions to validate the output
    assert len(list_of_dicts) == 2  # Only 2 students added because 1 was a duplicate
