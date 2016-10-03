#coding=utf8
from sh import tail
#Interactive callbacks



def process_output2(line, stdin, process):
    print(line)
    if "ERROR" in line:
        process.kill()
        return True

q = tail("-f", "/var/log/accountpolicy.log", _out=process_output2)
q.wait()
