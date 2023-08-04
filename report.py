# import package
import requests
import pandas as pd

# 爬取目標網站
year = 107
season = 4
stock_number = 2882

BalanceSheetURL = "https://mops.twse.com.tw/mops/web/t164sb03";      # 資產負債表
ProfitAndLoseURL = "https://mops.twse.com.tw/mops/web/ajax_t164sb04";    # 損益表
CashFlowStatementURL = "https://mops.twse.com.tw/mops/web/t164sb05"; # 現金流量表


def crawl_financial_Report(url):
    
    form_data = {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'co_id':stock_number,
        'year': year,
        'season': season,
    }

    r = requests.post(url,form_data)
    html_df = pd.read_html(r.text)[1].fillna("")
    return html_df

data = crawl_financial_Report(BalanceSheetURL)
data.to_csv('balancesheet.xlsx')