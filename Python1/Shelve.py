# encoding=utf-8
import shelve
import os
d = shelve.open('haha.text')
# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，

class Me(object):
    def __init__(self, n):
        self.n = n


# name = ['ha', 'e', '我']
d['1'] = '3'
d['2'] = Me('我')

d.close()
