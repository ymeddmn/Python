# coding=gbk
import argparse
import re
import urllib
from datetime import datetime

# 获取ip
def getip():
    url = 'http://jsonip.com'
    res = re.search('\d+\.\d+\.\d+\.\d+', urllib.urlopen(url, 5).read())
    if res:
        return res.group(0)
    return None


date = getip()
print(date)
