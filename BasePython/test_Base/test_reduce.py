#coding=utf8
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9])

print reduce(add, [1, 3, 5, 7, 9], 100)


print sum([1, 3, 5, 7, 9])


#把序列变换成整数
def fn(x, y):
    return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])



#把str转换为int
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


#提供第三个参数，第一次，初始字典为空，作为statistics的第一个参数，然后遍历lst,作为第二个参数，然后将返回的字典集合作为下一次的第一个参数
def statistics(dic,k):
  if not k in dic:
    dic[k] = 1
  else:
    dic[k] +=1
  return dic

lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
print reduce(statistics,lst,{})


#翻转序列
print reduce(lambda L, ele: [ele] + L, [1, 2, 3], [])
