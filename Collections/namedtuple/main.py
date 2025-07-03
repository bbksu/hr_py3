from collections import namedtuple

amount_of_students = int(input())
columns = input().split()
columns = " ".join(columns)
Student = namedtuple("Student", columns)
student_scores = []
average_score = 0
for i in range(amount_of_students):
    student_scores.append(Student._make(input().split()))
    average_score += int(student_scores[i].MARKS)    

print(format(average_score/amount_of_students, ".2f"))