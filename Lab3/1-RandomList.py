import random

data = [random.randint(0, 10) for i in range(50)]
for i in range(11):
    print(str(i) + ":" + " " + str(data.count(i)))
