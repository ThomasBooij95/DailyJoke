from datetime import datetime,date

def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
today = date.today().strftime("%Y-%m-%d")
date_str = '2020-04-12'
# date_begin = datetime.strptime(date_str, '%m-%d-%Y').date()
# begindate = datetime.strptime("2020-04-14","%Y-%m-%d")
print('today is ' ,today)
print('the begindate is ' ,date_str)
jokeNr = days_between(today,date_str)%100
print(jokeNr)


