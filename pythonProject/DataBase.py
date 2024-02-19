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
            if key in student.values():
                print("Student found.")
                return student
        return "Student not found."

    def update_student(self, key, **kwargs):
        for student in self.students:
            if key in student.values():
                student.update(kwargs)
                return "Student details updated successfully."
        return "Student not found."

    def delete_student(self, key):
        for student in self.students:
            if key in student.values():
                self.students.remove(student)
                return "Student removed successfully."
            else:
                return "Student not found."

    def save_to_file(self):
        pass

    def load_from_file(self):
        pass

db = Student()

db.add_student("John", 20, "A")
db.add_student("Alice", 21, "B")
print(db.view_students())

print(db.search_student("John"))

print(db.update_student("Alice", age=22))
print(db.view_students())

print(db.delete_student("John"))
print(db.view_students())