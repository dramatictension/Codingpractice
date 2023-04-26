student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total_height = 0
for height in student_heights:
    total_height = total_height + height

studentnumber = 0 
for student in student_heights:
    studentnumber = studentnumber + 1 

average_height = round(total_height / studentnumber)
print(average_height)
