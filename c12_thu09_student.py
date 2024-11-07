# group id (in LEB2): c12_thu09
# filename: c12_thu09_student.py
# 000 firstname lastname
# 999 firstname lastname

# change this imperative programming style 
# to object-oriented programming style 
# submission deadline: before midnight of Sun 10 Nov 2024
# (23:59 on Sunday 10 Nov 2024)

"""
Student Information System
* this application interact with users to store and retrieve student information
  -- the user can add student info (id, firstname, and lastname) into the database
  -- the user can search for student info in the database using student id
  -- the user can list all student info from the database
* the main function:
  -- create the database and call the main user interface
* the user interface functions:
  -- interact with the users
  -- know nothing about the data format, the data structure, and the database
* the business logic functions:
  -- do not interact with the users
  -- handle all the data format, the data structure, and database
"""

class StudentInfoSystem:
    def __init__(self, db):
        self.db = db

    def ui_main_menu(self):
        """
        Display the main menu and handle user input to perform actions
        on the student information system.
        """
        while True:
            print("\nStudent Information System")
            print("  [1] Add a student into the database.")
            print("  [2] Search for a student by id.")
            print("  [3] List all students.")
            result = input("  Choose one [1|2|3] or anything else to exit: ")
            try:
                result = int(result)
                if result == 1:
                    self.ui_add_student()
                elif result == 2:
                    self.ui_search_student()
                elif result == 3:
                    self.ui_list_students()
                else:
                    print("\nExit program normally.")
                    break
            except ValueError:
                break

    def ui_input_student_id(self) -> int:
        """
        Prompt the user for a valid student id input.
        Loops until a valid student id is entered.
        """
        while True:
            value = input("  Please type a valid student id and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            sid = self.transform_to_sid(value)
            if sid is not None:
                return sid
            print("  Invalid student id format.")

    def ui_input_new_student_id(self) -> int:
        """
        Prompt the user for a new student id that does not already exist in the database.
        Loops until a valid, unique id is entered.
        """
        while True:
            sid = self.ui_input_student_id()
            if self.get_student_by_id(sid) is None:
                return sid
            print("  This student id already exists.")

    def ui_input_student_name(self, name_type: str) -> str:
        """
        Prompt the user for a valid student name (either first name or last name).
        Loops until a valid name format is entered.
        """
        while True:
            value = input(f"  Please type the student {name_type} and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            if self.validate_name(value):
                return value
            print("  Invalid student name format (whitespace is not allowed).")

    def ui_add_student(self):
        """
        Prompt the user to input a student's id, first name, and last name,
        then add the student to the database.
        """
        print("Adding a student to the database:")
        try:
            sid = self.ui_input_new_student_id()
            firstname = self.ui_input_student_name("firstname")
            lastname = self.ui_input_student_name("lastname")
            self.add_student_to_db(sid, firstname, lastname)
            print(f"Student[{sid}: {firstname} {lastname}] added successfully.")
        except ValueError:
            print("  -- No student added --")

    def ui_search_student(self):
        """
        Prompt the user for a student id and search for that student in the database.
        Display the student's information if found.
        """
        print("Searching for a student by student id:")
        try:
            sid = self.ui_input_student_id()
            student = self.get_student_by_id(sid)
            if student is None:
                print("  Student not found.")
            else:
                print(f"  Student id: {sid}, Firstname: {student[0]}, Lastname: {student[1]}")
        except ValueError:
            print("  -- No student to search --")

    def ui_list_students(self):
        """
        List all students in the database and display their information.
        """
        students = self.get_all_students()
        if not students:
            print("  -- No students in the database --")
        for student in students:
            print(f"  Student id: {student[0]}, Firstname: {student[1]}, Lastname: {student[2]}")

    # Helper methods for database interaction
    def transform_to_sid(self, value: str) -> int:
        """Transform a string value into a valid student id."""
        try:
            return int(value)
        except ValueError:
            return None

    def validate_name(self, name: str) -> bool:
        """Validate the format of the name (no whitespace allowed)."""
        return ' ' not in name

    def add_student_to_db(self, sid: int, firstname: str, lastname: str):
        """Add a student to the database."""
        # Here we simulate adding the student to the database
        self.db[sid] = (firstname, lastname)

    def get_student_by_id(self, sid: int):
        """Get a student by their id from the database."""
        return self.db.get(sid)

    def get_all_students(self):
        """Get all students from the database."""
        return [(sid, student[0], student[1]) for sid, student in self.db.items()]


# Main execution function
def main():
    # Initialize the student database as a dictionary
    db = {}
    system = StudentInfoSystem(db)
    system.ui_main_menu()

if __name__ == "__main__":
    main()