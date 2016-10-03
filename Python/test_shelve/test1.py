#coding=utf8
import shelve
'''
简单的数据存储方案

shelve类似于一个key-value数据库，可以很方便的用来保存Python的内存对象，其内部使用pickle来序列化数据，简单来说，使用者可以将一个列表、字典、
或者用户自定义的类实例保存到shelve中，下次需要用的时候直接取出来，就是一个Python内存对象，不需要像传统数据库一样，先取出数据，然后用这些数
据重新构造一遍所需要的对象
'''

def test_shelve():
  # open 返回一个Shelf类的实例
  #
  # 参数flag的取值范围：
  # 'r'：只读打开
  # 'w'：读写访问
  # 'c'：读写访问，如果不存在则创建
  # 'n'：读写访问，总是创建新的、空的数据库文件
  #
  # protocol：与pickle库一致
  # writeback：为True时，当数据发生变化会回写，不过会导致内存开销比较大

  d = shelve.open('shelve.db', flag='c', protocol=2, writeback=False)

  assert isinstance(d, shelve.Shelf)

  d['abc'] = {'name': ['a', 'b']}  #在数据库中插入一条记录

  d.sync()

  print d['abc']


  d['abc']['x'] = 'x'  #writeback是False，因此对value进行修改是不起作用的
  print d['abc']

  d['abc'] = 'xxx'   #直接替换key的value还是起作用的
  print d['abc']

  d['abc'] = {'name': ['a', 'b']}   #还原abc的内容
  d.close()

  d = shelve.open('shelve.db', writeback=True)  #writeback为True时，对字段内容的修改会writeback到数据库中

  print d['abc']  #上面我们已经保存了abc的内容为{'name': ['a', 'b']}，打印一下看看对不对

  d['abc']['xx'] = 'xxx'  #修改abc的value的部分内容
  print d['abc']
  d.close()

  d = shelve.open('shelve.db')   #重新打开数据库，看看abc的内容是否正确writeback
  print d['abc']
  d.close()

if __name__ == '__main__':
    test_shelve()



