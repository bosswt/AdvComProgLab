file = open("score.csv", "r")
maximum = -1
file.readline()
for line in file:
    score = [int(x) for x in line.strip().split(",")][1:]
    if sum(score) > maximum:
        maximum = sum(score)
print("Highest total score is", str(maximum) + ".")
