####一维和多维列表
kongming = ['诸葛亮','蜀国',180,54]
print(kongming)
heros = [['曹操','魏','男',65] , ['武则天','周','女',82] , ['张良','汉','男',64] , ['成吉思汗','元','男',65]]
print(heros)
####打印
heroInfo = ['魏', '曹操', 160.3]
print(heroInfo[1])
heroInfos = [['魏', '曹操', 160.3], ['蜀', '刘备', 177.1], ['吴', '周瑜', 188.6]]
print(heroInfos[1][2])
####倒序
heroInfos = [['魏', '曹操', 160.3], ['蜀', '刘备', 177.1], ['吴', '周瑜', 188.6]]
print(heroInfos[-1][-1])
####新增
heros = []
heros.append('牛魔')
heros.insert(0, '妲己')
heros.insert(1, '兰陵王')
heros.insert(1, '亚瑟')
# 最终输出的结果为['妲己', '亚瑟', '兰陵王', '牛魔']
print(heros)
####删除
heros = ['牛魔', '妲己', '亚瑟', '兰陵王']
leave = heros.pop(1)
print('死亡英雄：' + leave)
print('存活英雄：' + str(heros))
leave = heros.pop(1)
print('死亡英雄：' + leave)
print('存活英雄：' + str(heros))
####修改
heros = ['牛魔', '妲己', '亚瑟', '兰陵王']
# 原始列表打印
heros = ['牛魔', '妲己', '亚瑟', '兰陵王']
# 原始列表打印
print('原来的英雄顺序为：' + str(heros))
# 下面需要完善
temp = heros[0]
heros[0] = heros[2]
heros[2] = temp
# 调整以后的列表打印
print('后来的英雄顺序为：' + str(heros))