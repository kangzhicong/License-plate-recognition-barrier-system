# -*- coding: UTF-8 -*-

import re                                                 #使用正则库

# 打开文件
fo = open("1.txt")    #hello.txt用于存放识别到的车牌
co = open("2.txt",'r',encoding='UTF-8')    #world.txt用于存放预先存储的车牌

colines = co.readlines()                       #读取所有world文件中的行

for line in fo.readlines():                        #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    matchObj = re.search(line, "%s" % colines, re.M | re.I)
   #正则匹配开始，使用search可以将全部符合条件的字符集都找出来
    if matchObj:
        print('车牌号：' + line)
    else :
        print('查无此车牌')

# 关闭文件
fo.close()
co.close()
