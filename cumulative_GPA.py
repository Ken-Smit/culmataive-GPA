class Student:
    def __init__(person, first_name, last_name):
        person.first_name = first_name
        person.last_name = last_name
        person.total_credits = 0
        person.total_quality_points = 0
        
    def add_course(person, credits, grade):
        person.total_credits += credits
        person.total_quality_points += credits * person.grade_to_point(grade)
        
    def calculate_gpa(person):
        if person.total_credits == 0:
            return 0.0
        return person.total_quality_points / person.total_credits
        
    def grade_to_point(person, grade):
        if grade == 'A':
            return 4.0
        elif grade == 'B':
            return 3.0
        elif grade == 'C':
            return 2.0
        elif grade == 'D':
            return 1.0
        else:
            return 0.0

# Prompting user for student's first and last name
first_name = input("Enter student's first name: ")
last_name = input("Enter student's last name: ")

# Creating a student object
student = Student(first_name, last_name)

# Prompting user for course credits and grades
while True:
    credits = float(input("Enter credits for the course (0 to end): "))
    if credits == 0:
        break
    grade = input("Enter grade for the course (A, B, C, D, F): ").upper()
    student.add_course(credits, grade)

# Displaying cumulative GPA
print(f"\nCumulative GPA for {student.first_name} {student.last_name}: {student.calculate_gpa()}")
