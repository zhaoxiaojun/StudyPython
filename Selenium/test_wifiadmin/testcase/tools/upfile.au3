ControlFocus("��","","Edit1")  ;ʶ��windows����

WinWait("[CLASS:#32770]","",10)  ;����10s���ڵȴ�������ʾ

ControlSetText("��","","Edit1","E:\Code\yzhselenium\test_wifiadmin\data\���.jpg")    ;���ļ�����������뱾���ļ���·��

Sleep(2000)    ;����2000ms

ControlClick("��","","Button1")   ;����ϴ������еĴ򿪰�ť