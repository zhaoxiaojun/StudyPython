ControlFocus("�ļ��ϴ�","","Edit1")  ;ʶ��windows����

WinWait("[CLASS:#32770]","",10)  ;����10s���ڵȴ�������ʾ

ControlSetText("�ļ��ϴ�","","Edit1","E:\Code\yzhselenium\test_163mail\data\logo.jpg")    ;���ļ�����������뱾���ļ���·��

Sleep(2000)    ;����2000ms

ControlClick("�ļ��ϴ�","","Button1")   ;����ϴ������еĴ򿪰�ť