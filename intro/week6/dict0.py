from cs50 import get_string, get_int

def main():
    students = [] # this is a list

    for _ in range(2):
        name = get_string("name: ")
        roll = get_int("Roll Number: ")

        students.append({"name":name, "roll": roll}) # create dictionary { key : value } 

    for student in students:
        print(f"{student['name']} has roll number {student['roll']}")

    for student in students:
        if student['name'] == 'Yuvraj':
            print(f"{student['name']} has roll number {student['roll']}")    

    print(students[1]['name'])

if __name__ == "__main__":
    main()