# -*- coding: utf-8 -*-
import re
import requests
import sys
import csv
import types
import operator
#reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)


para = {"Idc":"","Device":"","Org":"53","Keyword":"","MyFav":False,"Abnormal":False,"AppId":"","GroupKey":"","Domain":"","PoolId":""}

req = requests.post("http://webinfo.ctripcorp.com/Group/Search", json=para)
t = req.content.decode("utf-8")
soup = str(BeautifulSoup(t, "html5lib"))


p = re.findall(r'(?<=> )sg_jq.+(?=</div>)|Processor|\d* %|Memory|progress-bar-warning', soup)

#m=re.findall(r'(?<=<p>).+?(?=</p>)|(?<=<h2>).+?(?=</h2>)|(?<=<h3>).+?(?=</h3>)',ss)
s = re.compile(r"'(?=sg_jq)")

p3 = s.sub('\n', str(p))
#p1 = p3.replace(',', '')
#p1 = p3.splitlines()
#p2 = ''.join(p1)
#p4 = re.findall(r'.+', p3, re.S)
p4 = re.findall(r'.+(?=progress-bar-warning)', p3)
s1 = re.compile(r"(?=sg_jq)")
p5 = s1.sub('\n', str(p4))
@app.route('/')
def body():
    return p5

if __name__ == '__main__':
    app.run()

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
'''