#Enter student names and their scores below as Key: Value
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#Creating an empty dictionary called student_grades.
student_grades = {}

#for (every key) in student_scores
for student in student_scores:
#New var score = (value of key) of (key), evaluate the value within the score ranges
#And then, create a new key in empty dictionary of student_grades in the form of key: (evaluation of the score)
    score = student_scores[student]
    if score >=91:
        student_grades[student] = "Outstanding"
    elif score <91 and score >80:
        student_grades[student] = "Exceeds Expectations"
    elif score >70 and score <81:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
    
print(student_grades)