####字典
heroInfo = {
    'name': '曹操',
    'state': '魏',
    'weapon': '倚天剑',
    'mount': '爪黄飞电',
    'height': 160.1
}
print(heroInfo)

####字典访问
heroInfo = {
    'name': '张飞',
    'state': '蜀',
    'weapon': '丈八蛇矛',
    'mount': '王追',
    'height': 188.8
}
if 'weapon' in heroInfo:
    print(heroInfo['weapon'])

####key-value
info = {
    'name': '赵云',
    'state': '蜀',
    'weapon' : ['青釭剑', '亮银枪'],
    'mount': '照夜玉狮子'
}
print(info)

####字典增改
heroInfo = {'name': '赵云', 'state': '蜀', 'weapon': '亮银枪', 'mount': '照夜玉狮子'}
print('之前：' + str(heroInfo))
heroInfo['weapon'] = ['青釭剑','亮银枪']
heroInfo['hostage'] = '阿斗'
print('之后：' + str(heroInfo))

####字典删除
raiseList = {}
raiseList['关羽'] = '后将军'
raiseList['张飞'] = '左将军'
raiseList['马超'] = '右将军'
raiseList['黄忠'] = '后将军'
raiseList['关羽'] = '前将军'
raiseList['魏延'] = '镇远将军'
del raiseList['魏延']
print(raiseList)

####字典遍历
heroInfos = [
  {'name':'关羽','combat' : '99', 'position' : '前将军', 'weapon' : '青龙偃月刀', 'mount' :'赤兔'},
  {'name':'张飞','combat' : '98','position' : '左将军', 'weapon' : '丈八蛇矛', 'mount' : '王追'},
  {'name' : '马超','combat' : '98', 'position' : '右将军', 'weapon' : '虎头湛金枪','mount' : '里飞沙'},
  {'name' : '黄忠','combat' : '96','position' :'后将军','weapon' : ('凤嘴刀','三石弓'), 'mount' : '燎原火'},
  {'name' : '赵云', 'combat' : '99','position' : '征南将军','weapon' : ('青釭剑','亮银枪'),'mount' : '照夜玉狮子'}
]
print(heroInfos)

heroInfos = [{
    'name': '关羽',
    'combat': 99,
    'position': '前将军',
    'weapon': '青龙偃月刀',
    'mount': '赤兔',
}, {
    'name': '张飞',
    'combat': 98,
    'position': '左将军',
    'weapon': '丈八蛇矛',
    'mount': '王追',
}, {
    'name': '马超',
    'combat': 98,
    'position': '右将军',
    'weapon': '虎头湛金枪',
    'mount': '里飞沙',
}, {
    'name': '黄忠',
    'combat': 96,
    'position': '后将军',
    'weapon': ('凤嘴刀', '三石弓'),
    'mount': '燎原火',
}, {
    'name': '赵云',
    'combat': 99,
    'position': '征南将军',
    'weapon': ('青釭剑', '亮银枪'),
    'mount': '照夜玉狮子',
}]
list = []
sum =0;
for hero in heroInfos:
    list.append(hero['combat'])
    sum += hero['combat']
high = max(list)
low = min(list)
sum = sum/5;

list_high = []
list_low = ''
for hero in heroInfos:
    if hero['combat'] == high:
        list_high.append(hero['name'])
    if hero['combat'] == low:
        list_low = hero['name']
print('平均武力值'+str(sum))
print('武力值最高的是'+str(list_high))
print('武力值最低的是'+str(list_low))

####集合
heros = [
    '曹操',
    '夏侯惇',
    '刘备',
    '典韦',
    '刘备',
    '关羽',
    '牛魔',
    '妲己',
    '亚瑟',
    '兰陵王',
    '张飞',
    '夏侯惇',
    '关羽',
    '诸葛亮',
    '牛魔',
    '妲己',
    '亚瑟',
    '兰陵王',
    '周瑜',
    '孙策',
    '大乔',
    '小乔',
]
print(len(set(heros)))

####集合遍历增删
heros = set(['刘备', '关羽', '张飞', '赵云', '小乔', '周瑜', '大乔', '孙策', '刘备', '刘备'])
print('战斗之前：' + str(heros))
heros.remove('小乔')
heros.add('曹操')
heros.remove('张飞')
heros.remove('赵云')
heros.add('小乔')
print('战斗之后：' + str(heros))