import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import os

stocks_data = []
urlValue = ''
tableSelected = ''

#Remove the # from the line for which data is required
#e.g. for depreciation remove the # from 4th line below (ln18)

#whichData = 'Rev' #1
#whichData = 'COGS' #2
#whichData = 'EBIT' #3
#whichData = 'DEP' #4
#whichData = 'int' #5
whichData = 'netInc' #6
#whichData = 'lDebt' #7
#whichData = 'cLiab' #8
#whichData = 'cAssets' #9
#whichData = 'cash' #10
#whichData = 'div' #11
#whichData = 'CFo' #12
#whichData = 'Capex' #13

#it will automatically take the url for data such as cashflows, income statement and corresponding HTML table

if (whichData in ['DEP', 'CFo', 'Capex','div','cash']):
    if (whichData == 'DEP'):
        htmlTable = 16
    elif (whichData == 'CFo'):
        htmlTable = 79
    elif (whichData == 'Capex'):
        htmlTable = 213
    elif (whichData == 'cash'):
        htmlTable = 19
    elif (whichData == 'div'):
        htmlTable = 161
    urlValue = 'cash-flow'
    print('Casflow selected: ' + whichData)

elif (whichData in ['cAssets', 'cLiab', 'lDebt']):
    if (whichData == 'cAssets'):
        htmlTable = 55
    elif (whichData == 'cLiab'):
        htmlTable = 180
    elif (whichData == 'lDebt'):
        htmlTable = 192
    urlValue = 'balance-sheet'
    print('Balance sheet selected: ' + whichData)

elif (whichData in ['EBIT', 'Rev', 'COGS','netInc','int']):
    if (whichData == 'EBIT'):
        htmlTable = 47
    elif (whichData == 'Rev'):
        htmlTable = 2
    elif (whichData == 'COGS'):
        htmlTable = 8
    elif (whichData == 'netInc'):
        htmlTable = 89
    elif (whichData == 'int'):
        htmlTable = 53
    urlValue = 'financials'
    print('Income statement selected: ' + whichData)

#empty arrays for populating data to be converted to DataFrames
data_current = []
data_prev1 = []
data_prev2 = []
data_prev3 = []

#no_data array to populate incase data was skipped/missed during scraping
no_data = []

#stocks universe below
stocks = ['AAA','BBB','CCC',...]

def get_data():
    for stock in stocks:
        #automically takes the url necessary
        url = 'https://finance.yahoo.com/quote/' + stock + '/'+ urlValue + '?p=' + stock
        # Fetch the page that we're going to parse
        page = requests.get(url)
        # Parse the page with LXML, so that we can start doing some XPATH queries
        # to extract the data that we want
        tree = html.fromstring(page.content)
        # Using XPATH, fetch all table elements on the page
        table = tree.xpath('//div[@data-test="fin-row"]/div/div')

        if (len(table)>=htmlTable-1):
            stocks_data.append(stock)

            data_current.append(table[htmlTable].text_content())
            data_prev1.append(table[htmlTable+1].text_content())
            data_prev2.append(table[htmlTable+2].text_content())
            data_prev3.append(table[htmlTable+3].text_content())

        else:
            print(stock)
            no_data.append(stock)

get_data()

no_data_df = pd.DataFrame(no_data)
no_data_df.to_csv('no_data.csv')

#convert into dictionary then convert into DataFrame
dictionaryCreate = {'Name':stocks_data,'current':data_current, 'prev1':data_prev1,'prev2':data_prev2, 'prev3':data_prev3}

dataframeCreate = pd.DataFrame(dictionaryCreate)

#finally output data as CSV file
pd.DataFrame(dataframeCreate).to_csv('data.csv')
