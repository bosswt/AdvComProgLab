import pymongo

file = open("score.csv")

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0.5pvjy.mongodb.net/?retryWrites=true&w=majority"
)
studentDb = client.student_scores
documents = studentDb["scores"]
studentId = input("Please enter an id: ")
document = documents.find_one({"id": studentId})
print("Sum score:", document["sum"])

