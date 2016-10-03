#coding=utf8

#命名元组
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])   #命名元组 类
p = Point(1, 2)    #实例化类得到对象p
print p.x
print p.y
print '\n----------------------\n'

Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)
print p.x
print p.y
print p.z
print '\n----------------------\n'

isinstance(p, Point)    #True
isinstance(p, tuple)    #True  Point对象是tuple的一种子类



#继承命名元组
class Point(namedtuple('PointBase', ['x', 'y'])):
    __slots__ = ()
    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

p = Point(x=1.0, y=2.0)
q = Point(x=2.0, y=3.0)
sum = p + q
print sum.x, sum.y
print '\n----------------------\n'


#deque
'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
from collections import deque
q = deque(['a', 'b', 'c'])
print q

q.append('x')
print q
q.appendleft('y')
print q

q.pop()
print q
q.popleft()
print q
print '\n----------------------\n'


#defaultdict
'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict。 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1'] #key1存在
print dd['key2'] #key2不存在，返回默认值
print '\n----------------------\n'




#OrderedDict
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d     #dict的Key是无序的

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print  od             #OrderedDict的Key是有序的
print '\n----------------------\n'

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
list(od.keys())        #按照插入的Key的顺序返回
print '\n----------------------\n'


#实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
print '\n----------------------\n'


#Counter
'''
一个简单的计数器
'''
from collections import Counter   #际上也是dict的一个子类
c = Counter()
for ch in 'programming':
    print ch
    c[ch] = c[ch] + 1

print c
print '\n----------------------\n'
