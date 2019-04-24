import traceback
ls = []
try:
    with open('scores.csv', 'r') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            ls.append(row)
except:
    traceback.print_exc()

