ControlFocus("打开","","Edit1")  ;识别windows窗口

WinWait("[CLASS:#32770]","",10)  ;设置10s用于等待窗口显示

ControlSetText("打开","","Edit1","E:\Code\yzhselenium\test_wifiadmin\data\广告.jpg")    ;向文件名输入框输入本地文件的路径

Sleep(2000)    ;休眠2000ms

ControlClick("打开","","Button1")   ;点击上传窗口中的打开按钮