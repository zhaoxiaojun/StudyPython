#coding=utf8
from sh import ls
#Exit codes

output = ls("/")
print(output.exit_code) # should be 0


