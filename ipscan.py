#!/usr/bin/env python
#-*- coding:utf-8 -*-

import platform
import os
import time
import threading

def get_os():
   os = platform.system()
   if os == "Windows":
        return "n"
   else:
        return "c"

def ping_ip(ip_str):
     cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
     output = os.popen(" ".join(cmd)).readlines()

     flag = False
     for line in list(output):
         if not line:
            continue
         if str(line).upper().find("TTL") >=0:
            flag = True
            break
     if flag:
         print("ip: %s is ok ***"%ip_str)

def find_ip(ip_prefix):
    threads = []
    for i in range(1,255):
         ip = '%s.%s'%(ip_prefix,i)
         ta = threading.Thread(target=ping_ip, args=(ip,))
         threads.append(ta)

    for t in threads:
         t.start()

    t.join()

if __name__ == "__main__":
     print("start time %s"%time.ctime())
     commandargs = "172.22.232.1" # 要扫描的网段
     args = "".join(commandargs)

     ip_prefix = '.'.join(args.split('.')[:-1])
     find_ip(ip_prefix)
     print("end time %s"%time.ctime())
