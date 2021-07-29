#!/usr/bin/env python
#-*-coding:utf-8-*-
import re
import subprocess
from io import StringIO
import multiprocessing
import time
import sys
def check_alive(ip):
    result = subprocess.call('ping -w 1000 -n 1 %s' %ip,stdout=subprocess.PIPE,shell=True)
    if result == 0:
        h = subprocess.getoutput('ping ' + ip)
        returnnum = h.split('平均 = ')[1]
        with open('tong.txt','a') as f:
            f.write(ip)
        info = ('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
        print('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
        #return info
    else:
        #with open('notong.txt','a') as f:
        #    f.write(ip)
        info = ('\033[31m%s\033[0m ping 不通！' % ip)
        #return info
        #print('\033[31m%s\033[0m ping 不通！' % ip)
        print('\033[31m%s\033[0m ping 不通！' % ip)

if __name__ == '__main__':
    print("开始批量ping所有IP！")
    with open('ip.txt', 'r') as f:      #ip.txt为本地文件记录所有需要检测连通性的ip
        for i in f:
            p = multiprocessing.Process(target=check_alive, args=(i,))
            p.start()