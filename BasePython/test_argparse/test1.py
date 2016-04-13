#coding=utf8
#命令行解析工具argparse
import argparse

#在命令行中执行 python test1.py --help  python test1.py 4
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print args.square**2
