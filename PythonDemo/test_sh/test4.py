#coding=utf8
from sh import sleep
#非阻塞执行

# blocks
sleep(3)
print("...3 seconds later")



# doesn't block
p = sleep(3, _bg=True)
print("prints immediately!")
p.wait()
print("...and 3 seconds later")
