#coding=utf8
"""
模板方法模式
定义：定义一个操作中算法的框架，而将一些步骤延迟到子类中，使得子类可以不改变算法的结构即可重定义该算法中的某些特定步骤
类型：行为类模式
"""
class TestPaper:
    def TestQuestion1(self):
        print "Test1:A. B. C. D."
        print "(%s)" %self.Answer1()

    def TestQuestion2(self):
        print "Test1:A. B. C. D."
        print "(%s)" %self.Answer2()
    def Answer1(self):
        return ""
    def Answer2(self):
        return ""

class TestPaperA(TestPaper):
    def Answer1(self):
        return "B"
    def Answer2(self):
        return "C";

class TestPaperB(TestPaper):
    def Answer1(self):
        return "D"
    def Answer2(self):
        return "D";

if __name__ == "__main__":
    s1 = TestPaperA()
    s2 = TestPaperB()
    print "student 1"
    s1.TestQuestion1()
    s1.TestQuestion2()
    print "student 2"
    s2.TestQuestion1()
    s2.TestQuestion2()
