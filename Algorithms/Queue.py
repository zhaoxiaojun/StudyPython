#coding=utf8

class Queue:
   def __init__(self):
      self.items = []
   def is_empty(self):
      return self.items == []
   def enqueue(self, item):
      self.items.insert(0,item)
   def dequeue(self):
      return self.items.pop()
   def size(self):
      return len(self.items)


#双向队列
class Deque:
   def __init__(self):
      self.items = []
   def is_empty(self):
      return self.items == []
   def add_front(self, item):
       self.items.append(item)
   def add_rear(self, item):
      self.items.insert(0,item)
   def remove_front(self):
      return self.items.pop()
   def remove_rear(self):
      return self.items.pop(0)
   def size(self):
      return len(self.items)

if __name__ == '__main__':
    QO = Queue()
    QO.enqueue(2)
    QO.enqueue(3)
    print QO.dequeue()
