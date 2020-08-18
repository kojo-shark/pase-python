import datetime

def getDate(delta=1):
    today = datetime.datetime.today

    today = datetime.datetime.today()
yesterday =today - datetime.datetime(days=1)
datetime = yesterday.strftime("%m-%d-%Y")
