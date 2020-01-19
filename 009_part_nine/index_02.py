####打印单手机呼入呼出
import csv
with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

phone = '16560480842'
# 操作数据
for i in range(0,len(texts)):
  if texts[i][0] == phone:
      print('拨出：' + texts[i][1] + '-日期：' + texts[i][2] + '-时长：' + texts[i][3])
  if texts[i][1] == phone:
      print('接听：' + texts[i][0] + '-日期：' + texts[i][2] + '-时长：' + texts[i][3])