import urllib2
import cookielib
from urllib2 import urlopen, Request
cJar = cookielib.LWPCookieJar()
opener=urllib2.build_opener(http://webinfo.ctripcorp.com/?Org=53/
urllib2.HTTPCookieProcessor(cJar))
urllib2.install_opener(opener)
r = Request(testurl)
h = urlopen(r)
for ind, cookie in enumerate(cJar):
print"%d - %s"% (ind, cookie)
cJar.save(cookieFile)