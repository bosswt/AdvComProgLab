import pymongo
from dotenv import load_dotenv
import os
import json

load_dotenv()
MONGO = os.getenv("MONGO")

with open("stocks.json") as f:
    data = json.load(f)

client = pymongo.MongoClient(MONGO)
db = client.project

db.stocks.insert_many(data["stocks"])
