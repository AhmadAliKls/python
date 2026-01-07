marks_dict = {}

def removal_of_student(removing_name):
    if removing_name in marks_dict:
        removed = marks_dict.pop(removing_name)
        print(f"Removed {removing_name}: {removed}")
    else:
        print("Student not found.")
    return marks_dict

def update_marks(marks_dict, student_name, subject, new_marks):
    if student_name in marks_dict:
        if subject in marks_dict[student_name]:
            marks_dict[student_name][subject] = int(new_marks)
            print(f"Updated {subject} marks for {student_name} to {new_marks}")
        else:
            print("Invalid subject name.")
    else:
        print("Student not found.")
    return marks_dict

def calculate_average(marks_dict):
    average_marks = {}
    for student, marks in marks_dict.items():
        total = marks["maths"] + marks["physics"] + marks["computer"]
        average = total / 3
        average_marks[student] = average
    return average_marks

def accessing_student_marks(name):
    if name in marks_dict:
        marks = marks_dict[name]
        print(f"{name}'s marks → Maths: {marks['maths']}, Physics: {marks['physics']}, Computer: {marks['computer']}")
        return marks
    else:
        print("Student not found.")
        return None

while True:
    operation = input("\nChoose operation: accessing marks(am) / updating marks(um) / adding students(as) / removing student(rs) / average(a) / exit(e): ")

    if operation == "am":
        name_man = input("Enter name of student: ")
        accessing_student_marks(name_man)

    elif operation == "um":
        name_man = input("Enter name of student: ")
        subject = input("Enter subject (maths/physics/computer): ")
        new_marks = int(input("Enter new marks: "))
        marks_dict = update_marks(marks_dict, name_man, subject, new_marks)

    elif operation == "as":
        no_of_students = int(input("Enter number of students: "))
        for i in range(no_of_students):
            name = input("Enter name of student: ")
            maths = int(input("Enter marks in maths: "))
            physics = int(input("Enter marks in physics: "))
            computer = int(input("Enter marks in computer: "))
            marks_dict[name] = {"maths": maths, "physics": physics, "computer": computer}

    elif operation == "rs":
        removing_name = input("Enter name of student: ")
        removal_of_student(removing_name)

    elif operation == "a":
        averages = calculate_average(marks_dict)
        for student, avg in averages.items():
            print(f"{student}'s average marks: {avg}")

    elif operation == "e":
        print("Exiting program...")
        break

    else:
        print("Wrong choice")