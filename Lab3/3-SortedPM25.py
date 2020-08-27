file = open("pm25.csv")

pm = []
for line in file:
    temp = line.strip().split(",")[1]
    if temp != "-":
        pm.append(int(temp))

pm.sort(reverse=True)
for i in pm:
    print(i)
