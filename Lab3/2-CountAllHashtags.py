from collections import Counter

file = open("CH3Thailand Posts.csv")
lines = file.readlines()
hashtag = []
for line in lines:
    data = line.strip().split()
    hashtag += [x for x in data if x[0] == "#"]
print(Counter(hashtag).most_common())
