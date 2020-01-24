import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import os

stocks_data = []

cashflow_operating_2019 = []
cashflow_operating_2018 = []
cashflow_operating_2017 = []
cashflow_operating_2016 = []

cash_cash_eq_2019 = []
cash_cash_eq_2018 = []
cash_cash_eq_2017 = []
cash_cash_eq_2016 = []

current_asset_liabilities_2019 = []
current_asset_liabilities_2018 = []
current_asset_liabilities_2017 = []
current_asset_liabilities_2016 = []

div_2019 = []
div_2018 = []
div_2017 = []
div_2016 = []

long_term_debt_2019 = []
long_term_debt_2018 = []
long_term_debt_2017 = []
long_term_debt_2016 = []

capex_2019 = []
capex_2018 = []
capex_2017 = []
capex_2016 = []

interest_2019 = []
interest_2018 = []
interest_2017 = []
interest_2016 = []

oper_inc_2019 = []
oper_inc_2018 = []
oper_inc_2017 = []
oper_inc_2016 = []

no_data = []

stocks = ['AAA','BBB','CCC']

def get_data():
    for stock in stocks:

        #use only one url at a time as Yahoo starts blocking if too much traffic
        #cashflow_url = 'https://finance.yahoo.com/quote/' + stock + '/cash-flow?p=' + stock
        #balance_sheet_url = 'https://finance.yahoo.com/quote/' + stock + '/balance-sheet?p=' + stock
        income_statement_url = 'https://finance.yahoo.com/quote/' + stock + '/financials?p=' + stock
        # Fetch the page that we're going to parse
        #cashflow_page = requests.get(cashflow_url)
        #bs_page = requests.get(balance_sheet_url)
        income_page = requests.get(income_statement_url)
        # Parse the page with LXML, so that we can start doing some XPATH queries
        # to extract the data that we want
        #cashflow_tree = html.fromstring(cashflow_page.content)
        #bs_tree = html.fromstring(bs_page.content)
        inc_tree = html.fromstring(income_page.content)

        # Using XPATH, fetch all table elements on the page
        #cashflow_table = cashflow_tree.xpath('//div[@data-test="fin-row"]/div/div')
        #bs_table = bs_tree.xpath('//div[@data-test="fin-row"]/div/div')
        income_table = inc_tree.xpath('//div[@data-test="fin-row"]/div/div')

        if (len(income_table)>=80):
            stocks_data.append(stock)
            #forCashflowOperations
            '''cashflow_operating_2019.append(cashflow_table[79].text_content())
            cashflow_operating_2018.append(cashflow_table[80].text_content())
            cashflow_operating_2017.append(cashflow_table[81].text_content())
            cashflow_operating_2016.append(cashflow_table[82].text_content())'''

            #forCapex
            '''capex_2019.append(cashflow_table[213].text_content())
            capex_2018.append(cashflow_table[214].text_content())
            capex_2017.append(cashflow_table[215].text_content())
            capex_2016.append(cashflow_table[216].text_content())'''

            #forCashandCashEq
            '''cash_cash_eq_2019.append(bs_table[19].text_content())
            cash_cash_eq_2018.append(bs_table[20].text_content())
            cash_cash_eq_2017.append(bs_table[21].text_content())
            cash_cash_eq_2016.append(bs_table[22].text_content())'''

            #forCurrentAssets
            '''current_asset_liabilities_2019.append(bs_table[55].text_content())
            current_asset_liabilities_2018.append(bs_table[56].text_content())
            current_asset_liabilities_2017.append(bs_table[57].text_content())
            current_asset_liabilities_2016.append(bs_table[58].text_content())'''

            #forCurrentLiabilities
            '''current_asset_liabilities_2019.append(bs_table[180].text_content())
            current_asset_liabilities_2018.append(bs_table[181].text_content())
            current_asset_liabilities_2017.append(bs_table[182].text_content())
            current_asset_liabilities_2016.append(bs_table[183].text_content())'''

            #forLONGTERMDEBT
            '''long_term_debt_2019.append(bs_table[192].text_content())
            long_term_debt_2018.append(bs_table[193].text_content())
            long_term_debt_2017.append(bs_table[194].text_content())
            long_term_debt_2016.append(bs_table[195].text_content())'''

            #forOperIncome
            '''oper_inc_2019.append(income_table[47].text_content())
            oper_inc_2018.append(income_table[48].text_content())
            oper_inc_2017.append(income_table[49].text_content())
            oper_inc_2016.append(income_table[50].text_content())'''

            #forTotalRevenues
            '''oper_inc_2019.append(income_table[2].text_content())
            oper_inc_2018.append(income_table[3].text_content())
            oper_inc_2017.append(income_table[4].text_content())
            oper_inc_2016.append(income_table[5].text_content())'''

            #forCostofRevenue
            '''oper_inc_2019.append(income_table[8].text_content())
            oper_inc_2018.append(income_table[9].text_content())
            oper_inc_2017.append(income_table[10].text_content())
            oper_inc_2016.append(income_table[11].text_content())'''

            #forNetIncome
            oper_inc_2019.append(income_table[89].text_content())
            oper_inc_2018.append(income_table[90].text_content())
            oper_inc_2017.append(income_table[91].text_content())
            oper_inc_2016.append(income_table[92].text_content())

            #forInterest
            '''interest_2019.append(income_table[53].text_content())
            interest_2018.append(income_table[54].text_content())
            interest_2017.append(income_table[55].text_content())
            interest_2016.append(income_table[56].text_content())'''

            #forDividendsPaid
            '''div_2019.append(cashflow_table[161].text_content())
            div_2018.append(cashflow_table[162].text_content())
            div_2017.append(cashflow_table[163].text_content())
            div_2016.append(cashflow_table[164].text_content())'''

        else:
            print(stock)
            no_data.append(stock)

get_data()

no_data_df = pd.DataFrame(no_data)
no_data_df.to_csv('no_data.csv')

cashflows = {'Name':stocks_data,'2019':cashflow_operating_2019, '2018':cashflow_operating_2018,'2017':cashflow_operating_2017, '2016':cashflow_operating_2016}

capexs = {'Name':stocks_data,'2019':capex_2019, '2018':capex_2018, '2017':capex_2017, '2016':capex_2016}

cash_cash_eqs = {'Name':stocks_data,'2019':cash_cash_eq_2019, '2018':cash_cash_eq_2018, '2017':cash_cash_eq_2017, '2016':cash_cash_eq_2016}

long_term_debts = {'Name':stocks_data,'2019':long_term_debt_2019, '2018':long_term_debt_2018, '2017':long_term_debt_2017, '2016':long_term_debt_2016}

interests = {'Name':stocks_data,'2019':interest_2019, '2018':interest_2018, '2017':interest_2017, '2016':interest_2016}

op_incs = {'Name':stocks_data,'2019':oper_inc_2019, '2018':oper_inc_2018, '2017':oper_inc_2017, '2016':oper_inc_2016}

dividends= {'Name':stocks_data,'2019':div_2019, '2018':div_2018, '2017':div_2017, '2016':div_2016}

assets_liabilities= {'Name':stocks_data,'2019':current_asset_liabilities_2019, '2018':current_asset_liabilities_2018, '2017':current_asset_liabilities_2017, '2016':current_asset_liabilities_2016}

#cashflow = pd.DataFrame(cashflows)
#capex = pd.DataFrame(capexs)
#cash_cash_eq = pd.DataFrame(cash_cash_eqs)
#long_term_debt = pd.DataFrame(long_term_debts)
oper_inc = pd.DataFrame(op_incs)
#interest = pd.DataFrame(interests)
#dividend = pd.DataFrame(dividends)
#assets_liablity = pd.DataFrame(assets_liabilities)

pd.DataFrame(op_incs).to_csv('data.csv')
