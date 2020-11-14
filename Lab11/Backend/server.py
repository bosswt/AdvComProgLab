from flask import Flask
from flask import request
from flask import jsonify
from operator import itemgetter
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://admin:admin@cluster0.5pvjy.mongodb.net/retryWrites=true&w=majority"
)

studentDb = client.students


@app.route("/getscore")
def getScore():
    id = itemgetter("id")(dict(request.args))
    data = list(studentDb.scores.find({}, skip=int(id), limit=20))
    res = []
    for doc in data:
        temp = dict(doc)
        del temp["_id"]
        res.append(temp)
    print(len(res))
    response = jsonify({"data": res})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


app.run()
