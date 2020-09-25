import pymongo

file = open("score.csv")

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0.5pvjy.mongodb.net/?retryWrites=true&w=majority"
)
airbnbDb = client.sample_airbnb
documents = airbnbDb.listingsAndReviews.find({"address.country": "Brazil"})
for doc in documents:
    print(doc["name"] + ", Brazil")

