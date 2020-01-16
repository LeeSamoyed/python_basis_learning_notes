####变量赋值
# 进入霍格沃茨之前
epithet = '小白'
# 通过五年级“普通巫师等级”考试后
epithet = '普通巫师'
# 通过7年级“普通巫师等级”考试后
epithet = '终极巫师'
print(epithet)

####
name = 'LeeSamoyed'
school = 'nanjing institute of technology'
major = 'digital media of technology'
print(name)
print(school)
print(major)

####打印变量
# 入学年份
year = 2017
print(year)

####变量计算赋值
price = (7 + 15 + 5 + 80) * 5 * 1.05
print(price)

number = 3452
result = 0

####变量计算赋值
# 请补充转换逻辑的代码
result = (3 + 7) % 10 * 1000 + (4 + 7) % 10 * 100 + (5 + 7) % 10 * 10 + (2 + 7) % 10 * 1
print(result)

####str
print('| 物品 | 价格 |')
print('| 魔杖 | ' + str(17) +  '| ')

####
print("|  物品  |  价格  |")
price_sum = 0
object_count = 0
object = '魔杖'
price = 17
price_sum += price
object_count += 1
print('|  ' + object + '  |  ' + str(price) + '  |')
object = '坩埚'
price = 15
price_sum += price
object_count += 1
print('|  ' + object + '  |  ' + str(price) + '  |')
object = '长袍'
price = 80
price_sum += price
object_count += 1
print('|  ' + object + '  |  ' + str(price) + '  |')
object = '帽子'
price = 10
price_sum += price
object_count += 1
print('|  ' + object + '  |  ' + str(price) + '  |')
print('平均价格： ' + str(price_sum/object_count))
