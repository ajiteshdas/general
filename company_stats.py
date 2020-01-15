import pandas as pd
import lxml
import requests
from lxml import html

stocks = ['AAA','BBB,'CCC']
eps = [] #table[99]
bvps = [] #table[113]
sharesoutstanding = [] #table[37]

stocks_data = []

for stock in stocks:
    url = 'https://finance.yahoo.com/quote/'+stock+'/key-statistics?p='+stock
    page = requests.get(url)
    tree = html.fromstring(page.content)
    table = tree.xpath('//table/tbody/tr/td')

    stocks_data.append(stock)

    #for i in range(len(table)):
        #print(i," - ",table[i].text_content())
    eps.append(table[99].text_content())
    bvps.append(table[113].text_content())
    sharesoutstanding.append(table[37].text_content())

data = {'Name':stocks_data,'eps':eps, 'bvps':bvps,'sharesOut':sharesoutstanding}

pd.DataFrame(data).to_csv('data.csv')
