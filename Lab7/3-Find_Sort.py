import pymongo

file = open("score.csv")

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0.5pvjy.mongodb.net/?retryWrites=true&w=majority"
)
studentDb = client.student_scores
documents = studentDb.scores.find({"sum": {"$gt": 26}}).sort("sum", pymongo.DESCENDING)
for doc in documents:
    print(
        doc["id"],
        doc["quiz 1"],
        doc["quiz 2"],
        doc["quiz 3"],
        doc["quiz 4"],
        doc["quiz 5"],
        doc["sum"],
    )

