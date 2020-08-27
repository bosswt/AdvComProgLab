file = open("pm25.csv")

pm = []
for line in file:
    temp = line.strip().split(",")[1]
    if temp != "-":
        pm.append(int(temp))

print(sorted(pm, reverse=True))
