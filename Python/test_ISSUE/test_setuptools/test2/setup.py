#coding=utf8
from setuptools import setup, find_packages


setup(
    name = "demo",
    author = "Billy He",
    author_email = "billy@bjhee.com",
    description = "This is a sample package",
    license = "MIT",
    keywords = "hello world example",
    url = "http://example.com/HelloWorld/",   #项目主页
    version = "0.1",
    packages = find_packages('src'),   #包含所有src中的包
    #packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),  #通过exclude来排除一些特定的包
    package_dir = {'':'src'},   #告诉distutils包都在src下
    package_data = {
        '': ['*.txt'],  #包含任何包中含有.txt的文件
        'demo': ['data/*.dat'],  #包含demo包data文件夹中的 *.dat文件
    },
    include_package_data=True,    #启用清单文件MANIFEST.in
    exclude_package_date={'':['.gitignore']},  #排除某些包下的某些文件
    install_requires=[    #自动安装依赖依赖列表
        'Flask>=0.10',
        'Flask-SQLAlchemy>=1.5,<=2.1'
    ],
     dependency_links=[    #依赖包下载路径
        'http://example.com/dependency.tar.gz'
    ],
    long_description=__doc__,   #从代码中获取文档注释
)

