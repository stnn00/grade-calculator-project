# Python dictionary to store student name and grade data
student_grades = {
    "Anna Nguyen": [80, 83, 87],
    "Kaitlyn Nguyen": [89, 91, 98],
    "Jason Nguyen": [90, 80, 84],
    "Erick Santos": [68, 71, 70],
    "Zheng Yongkang": [90, 80, 84],
    "Benjy Fish": [71, 70, 70],
    "Lebron James": [85, 81, 88],
    "Jenna Ortega": [81, 74, 70],
    "Emma Myers": [80, 82, 74],
    "Zachary Patrone": [12, 10, 22],
    "Mia Crossing": [30, 10, 44],
    "KJ Apa": [81, 74, 89]
}

# Adding new key-value pairs (students, grades) into dictionary using a dictionary
transferring_students = {
    "Tyson Ngo": [91, 95, 98],
    "Charlie Golf": [75, 84, 70],
    "Miley Montana": [74, 80, 75]
}
student_grades.update(transferring_students)

# Removing students from dictionary using .pop() method
dismissed_students = ["Zachary Patrone", "Mia Crossing"]
for student in dismissed_students:
    student_grades.pop(student, None) # Added None to avoid any errors popping up when there are no dismissed students

student_averages = {} # Creating empty dictionary to fill with new calculated data
class_count = len(student_grades) # Using len() to calculate how many key-value pairs (students) are in student_grades
student_letter_grades = {} # Creating empty dictionary to fill with new calculated data
highest_average = 0
top_student = ""
passing_students = 0
failing_students = 0

for student, grade in student_grades.items(): # Iterating student_grades dictionary so I can work with each student data individually
    average_score = (sum(grade)//len(grade)) # Using sum() to find the sum of each student's grades, then using len() function to divide by how many grades they have (3). // is floor division to round down to the nearest whole number (integer)
    student_averages[student] = average_score # Adding individual average scores into student_averages dictionary

for student, average in student_averages.items():
    if 90 <= average <= 100:
        letter_grade = "A"
    elif 80 <= average <= 89:
        letter_grade = "B"
    elif 70 <= average <= 79:
        letter_grade = "C"
    elif 60 <= average <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"

    student_letter_grades[student] = letter_grade

    if average > highest_average:
        highest_average = average
        top_student = student
    if average >= 70:
        passing_students += 1
    elif average <= 69:
        failing_students += 1

list_averages = list(student_averages.values()) # Using list() to add all dictionary values into a list
total_sum = (sum(list_averages)) # Using sum() to total all the values (grade averages)
overall_average = int(total_sum / class_count) # Using int() to turn the float into an integer (whole number), can also use round() depending on grading system

print(f"The top performing student is {top_student} with the highest class average of {highest_average}!")
print(f"The overall class average is {overall_average}.")
print(f"{passing_students} students successfully passed the course!")

student_first_last = input("To check student's letter grade, enter their first and last name: ")

if student_first_last in student_letter_grades:
    print(f"{student_first_last}'s current letter grade is a {student_letter_grades[student_first_last]}.")
else:
    print(f'Student "{student_first_last}" does not exist in the registry. Please check the spelling and proper capitalization.')