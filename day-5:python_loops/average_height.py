student_heights = input("Input a list of student heights ").split()


for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(f"List of student heights {student_heights}")

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total student heights: {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Total number of students: {number_of_students}")


average_height = round(total_height/number_of_students)
print(f"The average student height is {average_height}")

