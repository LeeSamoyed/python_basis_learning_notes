import csv
with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

phone = '16560480842'
# 统计每个相关电话号码的总通话时长
# 字典存储每个相关号码的通话时长，key为电话号码，value为通话时长
duration = {}
for item in texts:
  callingPhone = item[0]  # 主叫号码
  calledPhone = item[1]  # 被叫号码

  # 判断是否为相关号码
  if phone == callingPhone or calledPhone == phone:

    # 下面三行逻辑，找到另一个号码，有可能是主叫，也可能是被叫
    otherPhone = calledPhone
    if phone == calledPhone:
      otherPhone = callingPhone

    # 如果字典中不存在号码通话总时长，则我们将其设置为0
    if otherPhone not in duration:
      duration[otherPhone] = 0

    # 字典中的通话时长总时长，往上累加
    duration[otherPhone] += int(item[3])

for key in duration:
  print('通话号码：' + key + '-总时长：' + str(duration[key] // 60) + '分钟')

# duration是字典，本身是无序的
# 我们需要用一个列表来存储相关的电话号码
sortCalled = []

# 排序处理
max= 0
for phone in duration:
    for phone_find in duration:
        if duration[phone_find] > max:
            max = duration[phone_find]
    for phone_sort in duration:
        if duration[phone_sort] == max:
            sortCalled.append({'phone':phone_sort,'sum':duration[phone_sort]})
            duration[phone_sort] = 0
            break
    max = 0

print('排序之后------------')
for item in sortCalled:
  print(item)