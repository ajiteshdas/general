#Author: Ajitesh Shankar Das
import nsepy #nsepy library by Swapnil Jariwala https://nsepy.readthedocs.io/en/latest/
from datetime import date, timedelta
import datetime
import pandas as pd

#stocks universe
stocks = ['AAA','BBB','CCC',...]
futures = []
d = []

#automatically sets the date range for the futures
if(today_datetime.weekday() >= 5):
    start = today_datetime.date() - timedelta(days=today_datetime.weekday() - 4)
elif(today_datetime.hour < 18):
    if(today_datetime.weekday() == 0):
        start = today_datetime.date() - timedelta(days=3)
    else:
        start = today_datetime.date() - timedelta(days=1)
else:
    start = today_datetime.date()

#automatically set the expiry date as last THURSDAY of current month for current contract
for i in range(25,31):
    if date(datetime.datetime.now().year,datetime.datetime.now().month,i).weekday() == 3:
       expiry_date =  date(datetime.datetime.now().year,datetime.datetime.now().month,i)

#get data for stocks using nsepy
for stock in stocks:
    data = nsepy.get_history(symbol=stock,start=start,end=start,expiry_date=expiry_date,futures=True)
    futures.append(data)

#calculate cash and carry arbitrage for each stock
for i in range(len(futures)):
    d.append((futures[i]['Settle Price'] - futures[i]['Underlying']) / futures[i]['Underlying']*100)

#append and publish data
d = pd.DataFrame(d)
stocks = pd.DataFrame(stocks)
futures = pd.concat([stocks,d], axis=1)

futures['stocks'] = stocks
futures['futures_arb'] = d

#get the maximum cash and carry arb: stock name and % returns
print(futures['stocks'][futures['futures_arb'].idxmax()]+':', '{:.2f}'.format(futures['futures_arb'][futures['futures_arb'].idxmax()])+'%')
