class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = {'name': name, 'age': age, 'grade': grade}
        self.students.append(student)
        return "Student added successfully."

    def view_students(self): 
        return self.students

    def search_student(self, key): 
        for student in self.students:
            if key.lower() in student['name'].lower():  # Case insensitive 
                print("Student found.")
                return student
        return "Student not found."

    def update_student(self, key, **kwargs):
        try:
            if (not kwargs):
                return "Error: No details provided to update."
            found_student = False
            for student in self.students:
                if key.lower() == student['name'].lower():  
                    found_student = True
                    # Check if the types of the new details match the types of the existing details
                    if all(isinstance(kwargs[value], type(student[value])) for value in kwargs):
                        for value in kwargs:
                            if value not in student:
                                return f"Invalid input: '{value}' is not a valid student detail."

                        student.update(kwargs)
                        return "Student details updated successfully.", student

            if not found_student:
                return "Student not found."
        except Exception as e:
            return f"Error occurred: {e}"

    def delete_student(self, key):
        found_student = False
        for student in self.students:
            if key.lower() == student['name'].lower():  # Case insensitive 
                found_student = True
                self.students.remove(student)
                return "Student removed successfully."

        if not found_student:
            return "Student not found."

    def save_to_file(self):
        pass

    def load_from_file(self):
        pass

db = Student()

db.add_student("John", 20, "A")
db.add_student("Alice", 21, "B")
print(db.view_students())

print(db.search_student("john"))

print(db.update_student())
print(db.view_students())

print(db.delete_student("John",age=21))
print(db.view_students())
