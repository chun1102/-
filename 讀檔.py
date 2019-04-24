file_path = '123.txt'
f = open(file_path, 'r')
#data = '軒弘是大笨蛋'
fr = f.read()
print(fr)
f.close()

# ------------------------------
# 寫入檔案
file_path = '123.txt'
f = open(file_path, 'w')
data = '軒弘是大笨蛋'
f.write(data)
f.close()
# ------------------------------
# 寫入檔案
file_path = '123.txt'
with open(file_path, 'r') as f:
    fr = f.read()
    print(fr)
# ------------------------------
import csv
file_path = 'df.csv'
with open(file_path, 'r', encoding='utf-8') as csvfile:
    # csv.reader(csvfile)
    rows = csv.DictReader(csvfile)

    for row in rows:
        print(row)

import json
members = [{'name': 'Eric'},
          {'name': 'Jacob'},
          {'name': 'Weihan'}]
obj = json.dumps(members)
print(obj)
from datetime import datetime
import locale
locale.setlocale(locale.LC_CTYPE,'chinese')
datestr = '2019-03-12 20:00:00'
dt = datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')
print(dt)
print(type(dt))
dstr = dt.strftime('%H時')
dstr1 = dt.strftime('%m/%d %H:%M')
print(dstr)
print(dstr1)