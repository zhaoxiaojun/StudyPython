#coding=utf8
#memory_profiler模块用来基于逐行测量代码的内存使用。使用这个模块会让代码运行的更慢
#安装：pip install memory_profiler
#另外，建议安装psutil包，这样memory_profile会运行的快一点：pip install psutil
#
#与line_profiler相似，使用@profile装饰器来标识需要追踪的函数。接着，输入：
#python -m memory_profiler timing_functions.py
#脚本的执行时间比以前长1或2秒。如果没有安装psutil包，也许会更长  内存使用是以MiB为单位衡量的，表示的mebibyte（1MiB = 1.05MB）
