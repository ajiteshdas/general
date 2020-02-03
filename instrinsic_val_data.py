import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import os

stocks_data = []
urlValue = ''
tableSelected = ''

#whichData = 'DEP'
#whichData = 'CFo' 
whichData = 'Capex'
#whichData = 'div'
#whichData = 'cAssets' 
#whichData = 'cLiab' 
#whichData = 'lDebt'
#whichData = 'EBIT' 
#whichData = 'Rev' 
#whichData = 'COGS'
#whichData = 'netInc'
#whichData = 'int'

if (whichData in ['DEP', 'CFo', 'Capex','div','cash']):
    if (whichData == 'DEP'):
        tableSelected = 16
    elif (whichData == 'CFo'):
        tableSelected = 79
    elif (whichData == 'Capex'):
        tableSelected = 213
    elif (whichData == 'cash'):
        tableSelected = 19
    elif (whichData == 'div'):
        tableSelected = 161
    urlValue = 'cash-flow'
    print('Casflow selected: ' + whichData)

elif (whichData in ['cAssets', 'cLiab', 'lDebt']):
    if (whichData == 'cAssets'):
        tableSelected = 55
    elif (whichData == 'cLiab'):
        tableSelected = 180
    elif (whichData == 'lDebt'):
        tableSelected = 192
    urlValue = 'balance-sheet'
    print('Balance sheet selected: ' + whichData)

elif (whichData in ['EBIT', 'Rev', 'COGS','netInc','int']):
    if (whichData == 'EBIT'):
        tableSelected = 47
    elif (whichData == 'Rev'):
        tableSelected = 2
    elif (whichData == 'COGS'):
        tableSelected = 8
    elif (whichData == 'netInc'):
        tableSelected = 89
    elif (whichData == 'int'):
        tableSelected = 53
    urlValue = 'financials'
    print('Income statement selected: ' + whichData)

data_current = []
data_prev1 = []
data_prev2 = []
data_prev3 = []

no_data = []
#stocks = ['AAA','BBB']

def get_data():
    for stock in stocks:
        #use only one url at a time as Yahoo starts blocking if too much traffic
        url = 'https://finance.yahoo.com/quote/' + stock + '/'+ urlValue + '?p=' + stock
        # Fetch the page that we're going to parse
        page = requests.get(url)
        # Parse the page with LXML, so that we can start doing some XPATH queries
        # to extract the data that we want
        tree = html.fromstring(page.content)
        # Using XPATH, fetch all table elements on the page
        table = tree.xpath('//div[@data-test="fin-row"]/div/div')

        if (len(table)>=tableSelected-1):
            stocks_data.append(stock)

            data_current.append(table[tableSelected].text_content())
            data_prev1.append(table[tableSelected+1].text_content())
            data_prev2.append(table[tableSelected+2].text_content())
            data_prev3.append(table[tableSelected+3].text_content())

        else:
            print(stock)
            no_data.append(stock)

get_data()

no_data_df = pd.DataFrame(no_data)
no_data_df.to_csv('no_data.csv')

dictionaryCreate = {'Name':stocks_data,'current':data_current, 'prev1':data_prev1,'prev2':data_prev2, 'prev3':data_prev3}

dataframeCreate = pd.DataFrame(dictionaryCreate)

pd.DataFrame(dataframeCreate).to_csv('data.csv')
