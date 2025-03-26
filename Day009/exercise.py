student_score={
    'Harry':88,
    'Ron':78,
    'Hermione':95,
    'Draco':75,
    'Nevile':60
}

student_grade={}

for student in student_score:
    if student_score[student] > 90:
        student_grade[student] = 'Outstanding'
    elif student_score[student] > 80:
        student_grade[student] = 'Exceeds Expectations'
    elif student_score[student] > 70:
        student_grade[student] = 'Acceptable'
    else:
        student_grade[student] = 'Fail'

print(student_grade)
print(student_score)
