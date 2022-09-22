import datetime
import time
import requests
from plyer import notification

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/Lithuania")
except:
    print("Check your internet connection")

if covidData is not None:
    data = covidData.json()['Success']

    while True:
        notification.notify(
         title = f'Covid 19 Stats on {datetime.date.today()}',
        message = f"Total cases : {data['cases']}\nToday cases : {data['todayCases']}\nToday deaths : {data['todayDeaths']}\nTotal active : {data['active']}",
         timeout = 50
        )
        # notify every 4 hours
        time.sleep(60*60*4)
