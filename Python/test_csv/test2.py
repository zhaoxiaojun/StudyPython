#coding=utf8
#写数据
import csv


# headers = ['Symbol','Price','Date','Time','Change','Volume']
# rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
#          ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
#          ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935001),
#        ]

# with open('stocks2.csv','w') as f:  #无需提前新建文件stocks2.csv
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)

#写字典序列
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open('stocks2.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
