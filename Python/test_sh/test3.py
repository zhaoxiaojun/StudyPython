#coding=utf8
from sh import curl
#from sh import adduser
#Keyword arguments  关键字参数


curl("http://www.baidu.com/", o="page.html", silent=True)

# or if you prefer not to use keyword arguments, this does the same thing:
#curl("http://www.baidu.com/", "-o", "page.html", "--silent")

# # resolves to "adduser amoffat --system --shell=/bin/bash --no-create-home"
# adduser("amoffat", system=True, shell="/bin/bash", no_create_home=True)

# # or
# adduser("amoffat", "--system", "--shell", "/bin/bash", "--no-create-home")
