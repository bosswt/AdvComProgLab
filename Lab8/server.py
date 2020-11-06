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


@app.route("/insertscore")
def insert():
    id, quiz1, quiz2, quiz3, quiz4, quiz5 = itemgetter(
        "id", "quiz1", "quiz2", "quiz3", "quiz4", "quiz5"
    )(dict(request.args))
    sum = int(quiz1) + int(quiz2) + int(quiz3) + int(quiz4) + int(quiz5)
    payload = {
        "id": id,
        "quiz 1": int(quiz1),
        "quiz 2": int(quiz2),
        "quiz 3": int(quiz3),
        "quiz 4": int(quiz4),
        "quiz 5": int(quiz5),
        "sum": sum,
    }
    studentDb.scores.insert_one(payload)
    return "OK"


@app.route("/findscore")
def find_score():
    id = itemgetter("id")(dict(request.args))
    data = dict(studentDb.scores.find_one({"id": id}))
    del data["_id"]
    response = jsonify({"data": data})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


app.run()
