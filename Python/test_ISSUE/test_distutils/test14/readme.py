#coding=utf8

'''
如果没有明确的列出需要发布的文件，则sdist命令默认在源码发布中包含下列文件：
由py_modules和packages选项指定的所有python源码文件；
由ext_modules或libraries选项指定的所有C源码文件；
由scripts指定的脚本；
测试脚本：test/test*.py；
README.txt (或者README)， setup.py 和setup.cfg；
package_data指定的所有文件；
data_files指定的所有文件。

如果还需要发布其他额外的文件，典型的做法是编写一个叫做MANIFEST.in的manifest模板。manifest模板包含如何创建MANIFEST文件的一系列指令，sdist命
令会解析该模板，根据模板中的指令，以及找到的文件生成MANIFEST(文件MANIFEST中明确的列出了包含在源码发布中的所有文件)

sdist命令的执行步骤如下：
if the manifest file (MANIFEST by default) exists and the first line does not have a comment indicating it is generated from MANIFEST.in, then it is used as is, unaltered;
if the manifest file doesn’t exist or has been previously automatically generated, read MANIFEST.in and create the manifest;
if neither MANIFEST nor MANIFEST.in exist, create a manifest with just the default file set;
use the list of files now in MANIFEST (either just generated or read in) to create the source distribution archive(s).

python setup.py sdist --manifest-only   #（重新）创建MANIFEST文件

'''
