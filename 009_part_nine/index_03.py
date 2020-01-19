####时长
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

phone = '16560480842'
# 操作数据
# str(int(int(texts[i][3])/60))
ph_ti = {}

for i in range(0, len(texts)):
    if texts[i][0] == phone:
        if texts[i][1] not in ph_ti:
            ph_ti[str(texts[i][1])] = int(texts[i][3])
        else:
            ph_ti[str(texts[i][1])] = ph_ti[str(texts[i][1])] + int(texts[i][3])
    if texts[i][1] == phone:
        if texts[i][0] not in ph_ti:
            ph_ti[str(texts[i][0])] = int(texts[i][3])
        else:
            ph_ti[str(texts[i][0])] = ph_ti[str(texts[i][0])] + int(texts[i][3])

for phone in ph_ti:
    print('通话号码：' + phone + '-总时长：' + str(int(ph_ti[phone]/60)) + '分钟')
