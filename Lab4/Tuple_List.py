file = open("score.csv")
student_score = []
for line in file:
    data = line.strip().split(",")
    score = sum([int(x) for x in data[1:]])
    data += [score]
    student_score.append(tuple(data))
for student in sorted(student_score):
    print(*student)
print("----")
for student in sorted(
    student_score, key=lambda student: (student[6], student[0]), reverse=True
):
    print(*student)
