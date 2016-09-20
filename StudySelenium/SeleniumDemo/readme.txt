Readme文件

更多信息，请联系作者，祝尚元（zhushangyuan@gmail.com）



一、eclipse项目的目录结构
SeleniumDemo：
├─bin         编译目录
├─UseCases    用例目录
├─lib         第三方jar文件
├─.settings   eclipse配置目录，自动生成
└─src         源文件夹
    └─dw          包名
        ├─xml       使用XML维护Selenium自动化测试脚本，包含dw.xml.DWloginXML.java
        └─junit     使用Selenium编写源代码，包含dw.junit. DWloginJUnit.java
        
        
二、关于依赖的第三方jar
为了减小附件的大小，本资源包不包括依赖的jar文件，请自行下载。下载下述两个jar文件放入lib文件夹下。

1. dom4j-1.6.1.jar  http://sourceforge.net/projects/dom4j/files/latest/download?source=files
2. selenium-server-standalone-2.25.0.jar  http://selenium.googlecode.com/files/selenium-server-standalone-2.25.0.jar


三、导入该eclipse java项目到eclipse工作区，即可运行。请注意构建路径的设置。