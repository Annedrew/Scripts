import requests
from bs4 import BeautifulSoup
import csv

"""
Euro(EUR): €
Dollar(usd): $
Pound(GBP): £
Krone(DKK): kr
Yuan(CNY): ¥
Ruble: ₽
"""
def get_exchange():
    # col = ['货币名称', '代码', '现汇买入价', '现钞买入价', '现汇卖出价', '现钞卖出价', '中行折算价']
    col_buy = ['货币名称', '代码', '银行现汇卖出价']
    col_sell = ['货币名称', '代码', '银行现汇买入价']
    row = ['欧元', '美元', '英镑', '丹麦克朗', '卢布']

    url='https://www.waihui580.com/'
    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, 'html.parser')
    all_cur = soup.find_all('tr')
    with open('buy_cus_exchange_rate.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(col_buy)
        for cur in all_cur:
            cur1 = cur.get_text(',')
            for r in row:
                if r in cur1: 
                    cur_list = cur1.split(',')
                    # 去掉特定符号：-
                    buy = cur_list[4]
                    con = cur_list[:2]
                    con.append(buy)
                    writer.writerow(con)
    with open('sell_cus_exchange_rate.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(col_sell)
        for cur in all_cur:
            cur1 = cur.get_text(',')
            for r in row:
                if r in cur1: 
                    cur_list = cur1.split(',')
                    # 去掉特定符号：-
                    sell = cur_list[2]
                    con = cur_list[:2]
                    con.append(sell)
                    writer.writerow(con)

    # 一行一行地写，一下子写很多行
    # writerow: 一下子写满, writerows