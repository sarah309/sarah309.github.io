# Python

def print_students(students):
    print('--------------------------Student Information--------------------------')
    for student in students:
        print(student)

FIRST_NAME_INDEX = 0
LAST_NAME_INDEX = 1
READING_INDEX = 2

def main():
    students = [
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8],
        ["Billy", "Bob", 6.3],
        ["Jeannie", "Roberts", 5.9],
        ["Bubba", "Bob", 7.9],
        ["Lilly", "Smith", 4.9]]
    
    print_students(students)

    last_name_sorted = sorted(students)
    print_students(last_name_sorted)

    first_name_sorted = sorted(students,key = lambda student_info : student_info[FIRST_NAME_INDEX])
    print_students(first_name_sorted)

    reading_sorted = sorted(students,key = lambda student_info : student_info[READING_INDEX], reverse = True)
    print_students(reading_sorted)
    

main()