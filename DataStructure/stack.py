#coding=utf8

class Stack:
    def __init__(self):
       self.items = []
    def is_empty(self):
       return self.items == []
    def push(self, item):
       self.items.append(item)
    def pop(self):
       return self.items.pop()
    def peek(self):
       return self.items[len(self.items)-1]
    def size(self):
       return len(self.items)

if __name__ == '__main__':
    SO = Stack()
    SO.push(2)
    SO.push(3)
    print SO.pop()
