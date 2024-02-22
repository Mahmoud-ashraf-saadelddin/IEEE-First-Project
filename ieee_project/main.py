import database


def main():
    def quit_or_not(flag):
        if flag == 1:
            flag = False
        else:
            flag = True
        return flag

    student_db = database.Student()
    print("--- welcome to Students data base ---")
    funcs = ["add_student", "view_students",
             "search_student", "update_student",
             "delete_student", "save_to_file",
             "load_from_file"]

    for i in range(7):
        print(f"{i + 1} : {funcs[i]}")

    print("-" * 20)
    print()
    flag = True
    while flag:

        case = int(input(f"choose the function you want "))
        print()
        if case == 1:
            name = input("enter studend name : ")
            age = input("enter studend age : ")
            grade = input("enter studend grade : ")
            student_db.add_student(name, int(age), grade)
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)

        elif case == 2:
            student_db.view_students()
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)
        elif case == 3:
            name = input("enter studend name : ")
            student_db.search_student(name)
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)
        elif case == 4:
            name = input("enter studend name you want to update : ")
            age = int(input("enter studend new age : "))
            grade = input("enter studend new grade : ")
            student_db.update_student(name, age=age, grade=grade)
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)
        elif case == 5:
            name = input("enter studend name you want to delete : ")
            student_db.delete_student(name)
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)
        elif case == 6:
            print(student_db.save_to_file())
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)
        elif case == 7:
            student_db.load_from_file()
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)
        else:
            print("invalid input ")
            check = bool(input("if you want to quit press any letter else press enter ").lower())
            if check:
                flag = quit_or_not(check)


if __name__ == "__main__":
    main()
