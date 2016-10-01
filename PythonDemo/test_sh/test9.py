#coding=utf8
from sh import ls
from sh import ssh
#Baking


ls = ls.bake("-la")
print(ls)

# resolves to "ls -la /"
print(ls("/"))

# calling whoami on a server
iam1 = ssh("root@192.168.3.2", "-p 22", "ifconfig")
print(iam1)

# resolves to "ssh root@192.168.3.2 -p 22 whoami"
myserver = ssh.bake("root@192.168.3.2", p=22)
print(myserver)

iam2 = myserver.whoami()
print(iam2)


# resolves to "sh root@192.168.3.2 -p 22  tail /root/InterfacePCTest/logs/test-account.log  -n 100"
iam3 = myserver.tail("/root/InterfacePCTest/logs/test-account.log", n=100)
print(repr(iam3))
