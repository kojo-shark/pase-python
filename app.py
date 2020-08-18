from flask import Flask, jsonify
import requests
import csv
from io import StringIO
import datetime
from lib.countries import countries
from lib.date import getDate

app = Flask(__name__)

url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"



def get_data(b_url, date):
    url = b_url + date + ".csv"
    res = requests.get(url)
    data = res.content.decode("ascii", "ignore")
    return StringIO(data)


def get_cases(url, countries):
    data = get_data(url)
    reader = csv.reader(data)
    cases = []

    for row in reader:
        if row[0] == "FIPS":
            continue
        if row[3] in countries:
            cases.append(
                {
                    "UpdatedOn": row[4].split(" ")[0],
                    "Country": row[3],
                    "Confirmed": row[7],
                    "Deaths": row[8],
                    "Recoveries": row[9],
                    "Active": row[10],
                }
            )
    return cases



def index():
    cases = get_cases(url, countries)
    return jsonify({"cases": cases})


    if country is None:
        cases = get_cases(url, countries)
        return {"cases": cases}
    
    cases = get_cases(url, date, countries)
    if case is None:
        return "not here"
    

# def index1():
#         country = requests.args.get("country")
#         date = request.args.get("data")

def mycheck():
    get_case(url, country)
    reader = csv.reader(data)

    if country not in countries:
        return None

    for row in reader:
        if row[3] == country.capitalize:
            return(
                {
                    "UpdatedOn": row[4].split(" ")[0],
                    "Country": row[3],
                    "Confirmed": row[7],
                    "Deaths": row[8],
                    "Recoveries": row[9],
                    "Active": row[10],
                }
            )
    else:
        return "Sorry country not found"
    
    
        

if __name__ == "__main__":
    app.run(debug=True)
