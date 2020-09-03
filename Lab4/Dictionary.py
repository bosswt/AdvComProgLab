file = open("CH3Thailand Posts.csv")
hashtag = {}
for line in file:
    data = line.strip().split()
    for text in data:
        if text[0] == "#":
            if text in hashtag:
                hashtag[text] += 1
            else:
                hashtag[text] = 1
print(hashtag)
