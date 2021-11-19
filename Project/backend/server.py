import pymongo
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()
MONGO = os.getenv("MONGO")

client = pymongo.MongoClient(MONGO)

db = client.project


@app.route("/stocks")
def stocks():
    data = list(db.stocks.find({}))
    for d in data:
        del d["_id"]
    response = dict()
    response["data"] = data
    return jsonify(response)


@app.route("/orders")
def getorders():
    data = list(db.orders.find({}))
    for d in data:
        del d["_id"]
    response = dict()
    response["data"] = data
    return jsonify(response)


@app.route("/orders", methods=["POST"])
def orders():
    body = request.json
    print(body)
    cart = body["cart"]
    for product in cart:
        print(product)
        db.stocks.update_one({"id": product["id"]}, {"$inc": {"qty": -product["qty"]}})
    db.orders.insert_one(body)
    return jsonify(sucess=True)


@app.route("/chart")
def chart():
    data = list(db.orders.find({}))
    stat = dict()
    for d in data:
        del d["_id"]
        for product in d["cart"]:
            if product["id"] in stat:
                stat[product["id"]] += 1
            else:
                stat[product["id"]] = 1
    data = dict()
    data["x"] = list(stat.keys())
    data["y"] = list(stat.values())
    print(data)
    return jsonify(data)


app.run()
