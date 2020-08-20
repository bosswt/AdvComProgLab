sentence = input("Input sentence: ")
count = 0
for c in sentence:
    if c.isdigit() or c.isalpha():
        count += 1
        print(c, end="")
print("\n" + str(count))
