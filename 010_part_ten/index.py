####利用 abs
#计算 | -2 | * |(10 - 20)| \
#在数学中 | -2 | = 2 表示取绝对值
answer = abs(-2) * abs(10-20)
print(answer)

#利用 sum
#1*1 + 2*2 + 3*3 + 4*4 + …… + 100 * 100
list = []
for i in range (1,101):
    list.append(i*i)
print(sum(list))

####