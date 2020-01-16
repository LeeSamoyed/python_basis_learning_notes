####马:1000米.第一步1米,后面每步2米
sum = 0
step = 1
sum += step
for i in range(1,int(1000/2)):
  step += 2
  sum += step
print(sum)

####妲己伤害累加 初始1000 后面每次加深250
sum = 0
basic = 1000
for i in range(0,7):
  sum += (basic+250*i)
print(sum)

####一共5000,每次450,650以下斩杀
ys = 5000
fw = 450
while(ys >650):
  ys -= fw
  print('斧王对亚瑟造成了450点伤害，亚瑟剩余生命值为' + str(ys) + '点')
print('斧王对亚瑟造成了650点伤害，亚瑟被击败')

####利用continue打印所有非蜀国
heroInfos = [['蜀', '刘备', 177.1], ['吴', '周瑜', 188.6], ['魏', '曹操', 160.3],
             ['蜀', '关羽', 212.4], ['蜀', '张飞', 188]]
for i in range(0,len(heroInfos)):
  if(heroInfos[i][0] == '蜀'):
    continue
  else:
    print(heroInfos[i][1])

####利用break打印第一个2m身高之前所有人名字
heroInfos = [['蜀', '刘备', 177.1], ['吴', '周瑜', 188.6], ['魏', '曹操', 160.3],
             ['蜀', '关羽', 212.4], ['蜀', '张飞', 188]]
for i in range(0,len(heroInfos)):
  if(heroInfos[i][2] < 200):
    print(heroInfos[i][1])
  else:
    break

####赵云被千军万马围住
for i in range(9):
  for j in range(9):
    if i == 4 and j == 4:
      print('云',end='')
    else:
      print('马',end='')
  print('')

####打印O
for i in range(9):
  for j in range(9):
    if i == j or i+j == 8:
      print('O',end='')
    else:
      print('*',end='')
  print('')

####回文判断
text = '上海自来水来自海上'
result = True # 表示是否为回文字符串
# 补充下面的代码，赋值给result
for i in range(int(len(text)/2)):
  if(text[i] != text[len(text)-1-i]):
    result = False
print(result)

####超过10个字符 + ...
sources = [
    '大小姐驾到，通通闪开！',
    '来一发吗？满足你！',
    '你，也是本小姐的粉丝吗？',
    '淑女什么的，才不屑呢！',
    '没人气的家伙，不值得浪费炮火！',
    '送你一个轰轰烈烈的退场，感谢本小姐大恩大德吧！',
    '除了炮弹，本小姐没别的跟你们交流了！',
    '百发百中！',
    '3，2，1，boom！',
    '哈哈哈，轰得不要太爽！',
    '野外徘徊的可怜家伙，能够收获的只有炮火！',
    '指哪打哪！',
    '来发子弹吗？满足你！',
    '饿啊~可恶！',
]
for i in range(0,len(sources)):
  if len(sources[i]) > 10 :
    print(sources[i][0:10] + '...')
  else:
    print(sources[i])
