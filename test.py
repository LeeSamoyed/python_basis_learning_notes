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