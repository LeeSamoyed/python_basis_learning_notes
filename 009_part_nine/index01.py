####提取主呼叫电话和被呼叫电话个数
import csv
with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)
  texts_in = []
  texts_in_in = []
  texts_pa = []
  texts_pa_pa = []
# 操作数据
for i in range(0,len(texts)):
  texts_in.append(int(texts[i][0]))
for i in range(0, len(texts)):
  texts_pa.append(int(texts[i][1]))

for i in texts_in:
  if i not in texts_in_in:
    texts_in_in.append(i)

for i in texts_pa:
  if i not in texts_pa_pa:
    texts_pa_pa.append(i)

print('主呼叫电话个数为' + str(len(texts_in_in)))
print('被呼叫电话个数为' + str(len(texts_pa_pa)))