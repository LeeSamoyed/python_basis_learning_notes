####if
character = '聪明'
if character == '勇敢':
  print('你的性格是' + character)  # 左侧缩进了4格
  print('格兰芬多！')  # 左侧缩进了4格
if character == '聪明':
  print('你的性格是' + character)  # 左侧缩进了4格
  print('拉文克劳！')  # 左侧缩进了4格
print('下一位')

####if、else
num = 3
if(num % 2 == 0):
  print('偶数')
else:
  print('奇数')
print('结束')

####if、elif、else
year = 2019
if(year % 400 == 0):
  print(str(year) + '年是闰年')
elif((year % 4 == 0) and (year % 100 != 0)):
  print(str(year) + '年是闰年')
else:
  print(str(year) + '年不是闰年')

score = 77
print('我的分数为：' + str(score))
if score >= 90 and score <= 100:
  print('层级为O')
elif score >= 70 and score < 90:
  print('层级为E')
elif score >= 60 and score < 70:
  print('层级为A')
elif score < 60:
  print('层级为P')
print('结束')