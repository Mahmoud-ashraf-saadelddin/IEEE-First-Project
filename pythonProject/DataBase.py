import csv

ID_creator = 1
class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        global ID_creator
        student = {'ID' : ID_creator, 'name': name, 'age': age, 'grade': grade}
        self.students.append(student)
        ID_creator+=1
        return "Student added successfully."

    def view_students(self):
        for k in self.students:
            print(k)

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

    def save_to_file(self, filename="student_db.csv"):
        # open a file to write
        with open(filename, 'w') as file:
            fieldnames = ['ID', 'name', 'age', 'grade']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.students)

        return "Data saved to file successfully."

    def load_from_file(self, filename="student_db.csv"):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    print(line)

            return "Data loaded from file successfully."
        except FileNotFoundError:
            return "File not found. No data loaded."
