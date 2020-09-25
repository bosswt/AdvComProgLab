import pymongo

file = open("score.csv")

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0.5pvjy.mongodb.net/?retryWrites=true&w=majority"
)
studentDb = client.student_scores

for row in file:
    data = row.strip().split(",")
    score = data[1:]
    scoreInt = [int(x) for x in score]
    payload = {
        "id": data[0],
        "quiz1": int(data[1]),
        "quiz2": int(data[2]),
        "quiz3": int(data[3]),
        "quiz4": int(data[4]),
        "quiz5": int(data[5]),
        "sum": sum(scoreInt),
    }
    studentDb.scores.insert_one(payload)
# studentDb.scores.insert_many(list_of_data,ordered=False)
