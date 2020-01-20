####利用 abs
# 计算 | -2 | * |(10 - 20)| \
# 在数学中 | -2 | = 2 表示取绝对值
answer = abs(-2) * abs(10 - 20)
print(answer)

# 利用 sum
# 1*1 + 2*2 + 3*3 + 4*4 + …… + 100 * 100
list = []
for i in range(1, 101):
    list.append(i * i)
print(sum(list))

#### 九九乘法表自定义函数
def multiTable(i):
    for x in range(i):
        for y in range(x + 1):
            print(str(x + 1) + '*' + str(y + 1) + '=' + str((x + 1) * (y + 1)), end=' ')
        print('')

# 下面为测试案例
multiTable(2)
multiTable(3)
multiTable(10)

####定义一个combat的方法
def combat(blood_f, blood_s):
    while blood_s > 650 and blood_f > 0:
        blood_s -= 450
        print('斧王对亚瑟造成了' + str(450) + '点伤害，亚瑟剩余生命值为' + str(blood_s) + '点')
        if blood_s <= 650:
            print('斧王对亚瑟造成了' + str(blood_s) + '点伤害，亚瑟被击败')
            break
        hurt = int(blood_f * 0.2 + 300)
        blood_f -= hurt
        if blood_f > 0:
            print('亚瑟对斧王造成了' + str(hurt) + '点伤害，斧王剩余生命值为' + str(blood_f) + '点')
        else:
            print('亚瑟对斧王造成了' + str(blood_f + hurt) + '点伤害，斧王被击败')

            break
print('第一场战斗---------------')
combat(5000, 5000)
print('第二场战斗---------------')
combat(5000, 3000)
# def combat(aex, arthur):
#     while arthur > 0 and aex > 0:
#         if arthur > 650:
#             arthur -= 450
#             print('斧王对亚瑟造成了' + str(450) + '点伤害，亚瑟剩余生命值为' + str(arthur) + '点')
#         else:
#             arthur -= 650
#             print('斧王对亚瑟造成了' + str(arthur + 650) + '点伤害，亚瑟被击败')
#             break
#
#         harm = int(aex * 0.2) + 300
#         aex -= harm
#         if aex > 0:
#             print('亚瑟对斧王造成了' + str(harm) + '点伤害，斧王剩余生命值为' + str(aex) + '点')
#         else:
#             print('亚瑟对斧王造成了' + str(harm + aex) + '点伤害，斧王被击败')
#             break

####切割
# 定义floor函数
def floor(num ,num_digit=2):
  num = str(num).split('.')
  num_int = num[0]
  num_decimal = num[1][0:num_digit]
  return str(num_int) + '.' +str(num_decimal)

print(floor(12.3456))
print(floor(12.3456, 3))

####立方
# 定义一个powOfSum的函数
def powOfSum(num , pow=2):
  sum = 0
  for i in range(0,len(num)):
    sum += num[i] ** pow
  return sum

print(powOfSum([1, 2, 3, 4, 5], 3))
print(powOfSum([1, 2, 3, 4, 5]))

####动态参数
# 请定义average函数
def average(*args):
  sum = 0
  for x in args:
    sum += x
  return sum/len(args)

print(average(1))
print(average(1, 2))
print(average(1, 2, 3, 4, 5))


####递归
# 斐波那契数列
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(10))

# 定义comat函数
def combat(n, m):
  if m <= 650:
    print('斧王对亚瑟造成了' + str(m) + '点伤害，亚瑟被击败')
    return True
  print('斧王对亚瑟造成了' + str(450) + '点伤害，亚瑟剩余生命值为' + str(m - 450) + '点')

  harm = int(n * 0.2 + 300)
  if n <= harm:
    print('亚瑟对斧王造成了' + str(n) + '点伤害，斧王被击败')
    return True
  print('亚瑟对斧王造成了' + str(harm) + '点伤害，斧王剩余生命值为' + str(n - harm) + '点')
  return combat(n - harm, m - 450)

print('第一场战斗---------------')
combat(5000, 5000)
print('第二场战斗---------------')
combat(5000, 3000)
