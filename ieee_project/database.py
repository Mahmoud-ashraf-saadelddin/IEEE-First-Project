import csv


class Student:
    def __init__(self):
        self.students = []
        self.last_id = self.get_last_id_from_file()  # Initialize last ID from file

    def add_student(self, name, age, grade):
        try:
            if not isinstance(name, str) or not isinstance(age, int) or not isinstance(grade, str):
                raise ValueError(
                    "Invalid input types. Name should be a string, age should be an integer, and grade should be a string.\n")
            if age < 0:
                raise ValueError("Age cannot be negative.\n")
            self.last_id += 1  # Increment last ID
            student = {'ID': self.last_id, 'name': name, 'age': age, 'grade': grade}
            self.students.append(student)
            return print("Student added successfully.\n")
        except ValueError as e:
            return print(str(e))

    def view_students(self):
        try:
            if not self.students:
                raise ValueError("No students to display.\n")
            print("The Full list of students: ")
            for student in self.students:
                print(student)
            print()
        except ValueError as e:
            print(str(e))

    def search_student(self, key):
        try:
            for student in self.students:
                if key.lower() in student['name'].lower():  # Case insensitive
                    print("Student found, Here is the data: ")
                    return print(f"{student}\n")
            return print("Student not found.\n")
        except Exception as e:
            return print(f"An error occurred during student search: {str(e)}\n")

    def update_student(self, key, **kwargs):
        try:
            if not kwargs:
                return print("Error: No details provided to update.\n")
            for student in self.students:
                if key.lower() == student['name'].lower():  # Case insensitive
                    # Check if the types of the new details match the types of the existing details
                    if all(isinstance(kwargs[value], type(student[value])) for value in kwargs):
                        for value in kwargs:
                            if value not in student:
                                return print(f"Invalid input: '{value}' is not a valid student detail.\n")
                        student.update(kwargs)
                        return print("Student details updated successfully.\n")
            return print("Student not found.\n")
        except Exception as e:
            return print(f"Error occurred: {e}\n")

    def delete_student(self, key):
        for student in self.students:
            if key.lower() == student['name'].lower():  # Case insensitive
                self.students.remove(student)
                return print("Student removed successfully.\n")
        return print("Student not found.\n")

    def clear_data(self):
        try:
            confirm = input("Are you sure you want to clear all data? (yes/no):  ").strip().lower()
            if confirm == "yes":
                self.students = []
                self.last_id = self.get_last_id_from_file()  # Reset last_id from file
                print("All data cleared successfully.\n")
            elif confirm == "no":
                print("Clear operation cancelled.\n")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

    def save_to_file(self, filename="student_db.csv"):
        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['ID', 'name', 'age', 'grade']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.students)
            return "Data saved to file successfully."
        except Exception as e:

            return f"Error occurred while saving to file: {e}"

    def load_from_file(self, filename="student_db.csv"):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
                # Print each student's information
                print("Data loaded from file successfully.")
                print("The Full list of students: ")
                for student in self.students:
                    print(student)
                print()

            return "Data loaded from file successfully."
        except FileNotFoundError:
            return "File not found. No data loaded."

    def get_last_id_from_file(self):
        try:
            with open("student_db.csv", 'r') as file:
                reader = csv.DictReader(file)
                # Check if there is data in the file
                if not any(reader):
                    return 0
                else:
                    # Find the maximum ID from the file
                    return max(int(row['ID']) for row in reader)
        except FileNotFoundError:
            return 0
