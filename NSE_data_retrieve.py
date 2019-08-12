import pandas as pd
from datetime import date, datetime , timedelta
from nsepy import get_history

todayte = datetime.today()
cmon = todayte.month
nmon = todayte.month + 1

#code below for near month data.

nthu = todayte
while todayte.month == cmon:
    todayte += timedelta(days=1)
    if todayte.weekday()==3 and todayte.month==cmon: #this is Thursday
        nthu = todayte


#start = pd.to_datetime('today').date()
#end = pd.to_datetime('today').date()

start = date(2019,7,1)
end = date(2019,7,25)
futures = True
expiry = date(nthu.year,nthu.month,nthu.day)

array = []

stockNames = ['ADANIPORTS','HCLTECH','IBULHSGFIN','SUNPHARMA','ZEEL','YESBANK','TECHM','INFY','UPL','BPCL','ICICIBANK','VEDL','HDFC','ITC','GAIL','AXISBANK','HINDPETRO','TCS','IOC','GRASIM','BAJFINANCE','TITAN','ULTRACEMCO','WIPRO','SBIN','BHARTIARTL','MARUTI','KOTAKBANK','ASIANPAINT','COALINDIA','LT','JSWSTEEL','TATAMOTORS','HDFCBANK','EICHERMOT','RELIANCE','CIPLA','INFRATEL','HINDUNILVR','TATASTEEL','HEROMOTOCO','M&M','NTPC','INDUSINDBK','BAJAJFINSV','BAJAJ-AUTO','POWERGRID','DRREDDY','HINDALCO','ONGC',]

for x in stockNames:
  temp = get_history(symbol=x, start=start, end=end, futures = futures, expiry_date = expiry)
  array.append(temp)

data = pd.concat(array)

print(data)
data.to_csv("~/Documents/Financial Analysis/NSE DATA_near.csv")

#Code below for far month data

nthu = todayte
while todayte.month == nmon:
    todayte += timedelta(days=1)
    if todayte.weekday()==3 and todayte.month==nmon: #this is Thursday
        nthu = todayte

#start = pd.to_datetime('today').date()
#end = pd.to_datetime('today').date()

expiry = date(nthu.year,nthu.month,nthu.day)

array =[]
for x in stockNames:
  temp = get_history(symbol=x, start=start, end=end, futures = futures, expiry_date = expiry)
  array.append(temp)

data = pd.concat(array)
print(data)
data.to_csv("~/Documents/Financial Analysis/NSE DATA_mid.csv")