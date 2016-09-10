#coding=utf8
import os


def VisitDir(path):
    print list(os.walk(path))
    for root,dirs,files in os.walk(path):
        for file in files:
            print os.path.join(root,file)


if __name__=="__main__":
    path="/opt"
    VisitDir(path)



"""
函数声明：walk(top,topdown=True,onerror=None)
1>参数top表示需要遍历的目录树的路径
2>参数topdown的默认值是"True",表示首先返回目录树下的文件，然后在遍历目录树的子目录.Topdown的值为"False"时，则表示先遍历目录树的子目录，返回子目录下的文件，最后返回根目录下的文件
3>参数onerror的默认值是"None",表示忽略文件遍历时产生的错误.如果不为空，则提供一个自定义函数提示错误信息后继续遍历或抛出异常中止遍历
4>该函数返回一个元组，该元组有3个元素，这3个元素分别表示每次遍历的路径名，目录列表和文件列表
"""
