file = open("pm25.csv", "r")
maximum = -1
maxDate = ""
for line in file:
    data = line.strip().split(",")
    if data[1] != "-":
        pm = int(data[1])
    date = data[0]
    if pm > maximum:
        maximum = pm
        maxDate = date
print("The higest pm2.5 is", str(maximum) + ".")
print("The higest date/time is", str(maxDate) + ".")
