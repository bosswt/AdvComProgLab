import requests

request = requests.get(
    "http://api.openweathermap.org/data/2.5/forecast?zip=10330,th&APPID=7743f38ce634083abe786e2d679955e3&units=metric"
)
data = dict(request.json())
max_date = ""
max_temp = 0
for time in data["list"]:
    if time["main"]["temp_max"] > max_temp:
        max_temp = time["main"]["temp_max"]
        max_date = time["dt_txt"]
print(max_date, max_temp)
