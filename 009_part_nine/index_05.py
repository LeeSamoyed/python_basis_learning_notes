import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# 获取拨出电话累计时长最长的手机号码
ph_ti = {}

for i in range(0, len(texts)):
    if texts[i][0] not in ph_ti:
        ph_ti[str(texts[i][0])] = int(texts[i][3])
    else:
        ph_ti[str(texts[i][0])] = ph_ti[str(texts[i][0])] + int(texts[i][3])
phone_max = ''
max = 0
for phone in ph_ti:
    if max < int(ph_ti[phone]):
        phone_max = phone
        max = int(ph_ti[phone])
print('最长通话时长主叫号码：' + phone_max + '，时长为：' + str(int(max/60)) + '分钟')
