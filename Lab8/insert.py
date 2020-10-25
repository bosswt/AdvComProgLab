import requests

file = open("score.csv", "r")

for line in file:
    data = line.strip().split(",")
    data[1:] = [int(i) for i in data[1:]]
    keys = ["id", "quiz1", "quiz2", "quiz3", "quiz4", "quiz5"]
    request_params = dict(zip(keys, data))
    requests.get("http://127.0.0.1:5000/insertscore", params=request_params)
