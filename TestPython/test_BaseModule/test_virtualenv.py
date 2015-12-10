#coding=utf8



#创建目录
#Mac:~ michael$ mkdir myproject
#Mac:~ michael$ cd myproject/
#Mac:myproject michael$

#创建一个独立的Python运行环境，命名为venv
#加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，
virtualenv --no-site-packages venv


#进入该环境
source venv/bin/activate


#退出当前的venv环境  回到正常的环境
deactivate
