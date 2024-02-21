import DataBase

student_db = DataBase.Student()

"""""
Manual test results

student_db.add_student("John", 20, "A")
student_db.add_student("Alice", 21, "B")
student_db.view_students()

student_db.search_student("John")

student_db.update_student("Alice", age=22)
student_db.view_students()

student_db.delete_student("John")
student_db.view_students()

student_db.save_to_file() #save current data 

student_db.clear_data() #clear list
student_db.view_students() #should be empty

student_db.load_from_file() #load deleted data
student_db.view_students()  #data returned

"""""

# Case 1: Adding a student with valid input.
print("Case 1: Adding a student with valid input.")
student_db.add_student("Alice", 20, "A")

# Case 2: Adding a student with invalid input types.
print("Case 2: Adding a student with invalid input types.")
student_db.add_student(123, "20", "A+")

# Case 3: Adding a student with a negative age.
print("Case 3: Adding a student with a negative age.")
student_db.add_student("Bob", -22, "B")

# Case 4: Viewing students when there are no students.
print("Case 4: Viewing students when there are no students.")
student_db.view_students()

# Case 5: Viewing students when there are existing students.
print("Case 5: Viewing students when there are existing students.")
student_db.add_student("Charlie", 21, "C")
student_db.add_student("David", 19, "B")
student_db.view_students()

# Case 6: Searching for a student by name with a match.
print("Case 6: Searching for a student by name with a match.")
student_db.search_student("Charlie")

# Case 7: Searching for a student by name without a match.
print("Case 7: Searching for a student by name without a match.")
student_db.search_student("Eve")

# Case 8: Updating a student's details with valid input.
print("Case 8: Updating a student's details with valid input.")
student_db.update_student("Alice", age=21, grade="A+")

# Case 9: Updating a student's details with invalid input type.
print("Case 9: Updating a student's details with invalid input type.")
student_db.update_student("Bob", age="22")

# Case 10: Updating a student's details with a non-existing detail.
print("Case 10: Updating a student's details with a non-existing detail.")
student_db.update_student("David", gender="Male")

# Case 11: Deleting an existing student.
print("Case 11: Deleting an existing student.")
student_db.delete_student("Charlie")

# Case 12: Deleting a non-existing student.
print("Case 12: Deleting a non-existing student.")
student_db.delete_student("Eve")

# Case 13: Clearing all data.
print("Case 13: Clearing all data.")
student_db.clear_data()

# Case 14: Saving data to a file.
print("Case 14: Saving data to a file.")
student_db.add_student("Frank", 25, "B")
student_db.add_student("Grace", 23, "A")
student_db.save_to_file("student_database.json")

# Case 15: Loading data from a file.
print("Case 15: Loading data from a file.")
student_db.clear_data()
student_db.load_from_file("student_database.json")
student_db.view_students()

# Case 16: Loading data from a non-existing file.
print("Case 16: Loading data from a non-existing file.")
student_db.load_from_file("non_existing_file.json")

# Case 17: Loading data from a file with invalid JSON format.
print("Case 17: Loading data from a file with invalid JSON format.")
with open("invalid_json_file.json", "w") as f:
    f.write("Invalid JSON format")
student_db.load_from_file("invalid_json_file.json")
