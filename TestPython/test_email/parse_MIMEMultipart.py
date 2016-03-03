#coding=utf8
import sys, email, time
from email import Utils


def printmsg(msg, level=0):
    l = "| " * level
    l2 = l + "|"
    print l + "+ Message Header: "
    for header, value in msg.items():
        print l2, header + ':', value
    if msg.is_multipart():
        for item in msg.get_payload():
            printmsg(item, level+1)

#msg = email.message_from_file(sys.stdin)
fp = open('email.data', 'r+')
msg = email.message_from_file(fp)

printmsg(msg)
