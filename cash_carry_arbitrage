import nsepy
from datetime import date, timedelta
import pandas as pd

#stocks universe
stocks = ['AAA','BBB','CCC',....]
futures = []
arb = []

start = pd.to_datetime('today').date() - timedelta(days=1)
end = pd.to_datetime('today').date() - timedelta(days=1)

#get data for stocks using nsepy
for stock in stocks:
    data = nsepy.get_history(symbol=stock,start=start,end=start,expiry_date=date(2019,11,28),futures=True)
    futures.append(data)

#calculate cash and carry arbitrage for each stock
for i in range(len(futures)):
    arb.append((futures[i]['Settle Price'] - futures[i]['Underlying']) / futures[i]['Underlying']*100)

#append and publish data
arb = pd.DataFrame(arb)
stocks = pd.DataFrame(stocks)
futures = pd.concat([stocks,arb], axis=1)

futures['stocks'] = stocks
futures['futures_arb'] = arb

#get the maximum cash and carry arb: stock name and % returns
print(futures['stocks'][futures['futures_arb'].idxmax()]+':', '{:.2f}'.format(futures['futures_arb'][futures['futures_arb'].idxmax()])+'%')
