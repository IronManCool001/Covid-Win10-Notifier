import requests
from datetime import date
import datetime

def confirmed_cases(country):
    current_date = date.today()
    previous_date = datetime.date.today() - datetime.timedelta(days=1)   
    previousdate = str(previous_date)
    country = country.lower()
    URL = f"https://api.covid19api.com/country/{country}/status/confirmed/live?from={current_date}15T00:00:00Z"
    response = requests.get(URL)
    response_json = response.json()
    for i in response_json:
        if previousdate in i['Date']:
            confirmed_cases.confirmed = i['Cases']
            print(f"Confirmed Cases: {confirmed_cases.confirmed}")


