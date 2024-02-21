import csv
import json

ID_creator = 1
class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        global ID_creator
        try:
            if not isinstance(name, str) or not isinstance(age, int) or not isinstance(grade, str):
                raise ValueError(
                    "Invalid input types. Name should be a string, age should be an integer, and grade should be a string.\n")
            if age < 0:
                raise ValueError("Age cannot be negative.\n")
            student = {'ID' : ID_creator,'name': name, 'age': age, 'grade': grade}
            self.students.append(student)
            ID_creator+=1
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
            if (not kwargs):
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
        self.students = []
        return print("All data cleared successfully.\n")

    # def save_to_file(self, filename="student_db.csv"):
    #     with open(filename, 'w') as file:
    #         fieldnames = ['ID','name', 'age', 'grade']
    #         writer = csv.DictWriter(file, fieldnames=fieldnames)
    #         writer.writeheader()
    #         writer.writerows(self.students)
    #     return print("Data saved to file successfully.\n")

    def save_to_file(self, filename="student_db.json"):
        with open(filename, 'w') as f:
            json.dump(self.students, f)
        return print("Data saved to file successfully.\n")
    
    # def load_from_file(self, filename="student_db.csv"):
    #     try:
    #         with open(filename, 'r') as file:
    #             reader = csv.DictReader(file)
    #             for line in reader:
    #                 print(line)
    #         return print("Data loaded from file successfully.\n")
    #     except FileNotFoundError:
    #         return print("File not found. No data loaded.\n")

    def load_from_file(self, filename="student_db.json"):
        try:
            with open(filename, 'r') as f:
                self.students = json.load(f)
            return print("Data loaded from file successfully.\n")
        except FileNotFoundError:
            return print("File not found. No data loaded.\n")
        except json.decoder.JSONDecodeError:
            return print("Invalid JSON format in file.\n")
