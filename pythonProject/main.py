import DataBase

db = DataBase.Student()
#
db.add_student("omar", -9, "A")
db.add_student("khaled", 20, "B")
db.add_student("mahmoud", 21, "C")
db.add_student("Ali", 23, "B")
db.view_students()
#
# print(db.search_student("John"))
#
# print(db.update_student("Alice", age=22))
# print(db.view_students())
#
# print(db.delete_student("John"))
# print(db.view_students())
# print(db.save_to_file())
# print(db.load_from_file())
# db.add_student("omar", 12, "A")
# db.view_students()