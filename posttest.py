# -*- coding: utf-8 -*-
import re
import requests
import sys
import csv
import types
import operator
import os
import time

reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)


para = {"Idc":"","Device":"","Org":"53","Keyword":"","MyFav":False,"Abnormal":False,"AppId":"","GroupKey":"","Domain":"","PoolId":""}

req = requests.post("http://webinfo.ctripcorp.com/Group/Search", json=para)
t = req.content.decode("utf-8")
soup = str(BeautifulSoup(t, "html5lib"))


p = re.findall(r'(?<=> )sg_.+(?=</div>)|(?<=> )route_.+(?=</div>)|(?<=> )gs.+(?=</div>)|Processor|\d* %|Memory|progress-bar-warning|progress-bar-danger', soup)

#m=re.findall(r'(?<=<p>).+?(?=</p>)|(?<=<h2>).+?(?=</h2>)|(?<=<h3>).+?(?=</h3>)',ss)
s = re.compile(r"'(?=sg_)|'(?=route_)|'(?=gs)")
time = '获取数据时间为' + time.strftime('%Y-%m-%d %H:%M:%S')

p3 = s.sub('\n', str(p))
#p1 = p3.replace(',', '')
#p1 = p3.splitlines()
#p2 = ''.join(p1)
#p4 = re.findall(r'.+', p3, re.S)
p4 = re.findall(r'.+(?=progress-bar-warning)|.+(?=progress-bar-danger)', p3)
#s1 = re.compile(r"(?=sg_)")
p5 = s.sub('\n', str(p4))
p6 = p5.replace('\"', '<br>')
p7 = p6.replace('[', '<br><h1 align="center">攻略集群服务器CPU内存报警看板</h1><br>')
p8 = p7.replace(']', '<br><br><a href="http://webinfo.ctripcorp.com/?Org=53" target="_blank"><strong>详细日志信息点此进入，</strong></a>')
p9 = p8.replace('\'', '&ensp;')
p10 = p9.replace(',', '&ensp;')
p11 = p10 + time
@app.route('/')

def body():
    return p11

if __name__ == '__main__':

    app.debug = False
    app.run(host='0.0.0.0', port=50002)


'''
with open('d:\\python27\\1.csv', 'wb') as c:
    w = csv.writer(c, delimiter=',', dialect='excel')

    w.writerows(p3)
    c.close()

#p3 = operator.itemgetter(2)
'''
'''
for m in p.finditer(soup):
    print m.group()

fp = open("d:\\python27\\web.txt", "w")
fp.write(p2) #写入数据

fp.close() #关闭文件
time.strftime('%Y-%m-%d %H:%M:%S')
'''