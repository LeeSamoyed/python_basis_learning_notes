import csv
with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

# 查询骚扰电话
# 先分开统计，每个主呼叫电话的通话记录
# callDict 的 key 为电话号码，value 为一个数组，表示所有的通话记录
callDict = {}
for item in texts:
  callingPhone = item[0]
  if callingPhone not in callDict:
    callDict[callingPhone] = []
  callDict[callingPhone].append(item)

# 遍历每个电话的通话记录
for key in callDict:
  calls = callDict[key]
  # num为统计小于10s的通话次数
  num = 0
  for call in calls:
    if int(call[3]) < 10:
      num += 1

  # 判断概率
  if num / len(calls) > 0.8:
    print(key + '是骚扰电话')
