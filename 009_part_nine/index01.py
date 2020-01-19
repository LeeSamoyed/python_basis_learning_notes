import csv
with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)
  text_in = []
  text_in_in = []
  text_pa = []
  text_pa_pa = []
# 操作数据
for i in range(0,len(texts)):
  text_in.append(int(texts[i][0]))
for i in range(0, len(texts)):
  text_pa.append(int(texts[i][1]))

for i in text_in:
  if i not in text_in_in:
    text_in_in.append(i)

for i in text_pa:
  if i not in text_pa_pa:
    text_pa_pa.append(i)

print('主呼叫电话个数为' + str(len(text_in_in)))
print('被呼叫电话个数为' + str(len(text_pa_pa)))