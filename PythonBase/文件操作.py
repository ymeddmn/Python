# coding=gbk

info = {
    1: '1',
    2: '1'
}

# o = open('a.text', 'w')
# o.write(str(info))  # 写文件
# o.close()


oread = open('a.text', 'r')
data = eval(oread.read())  # 读文件，eval是反序列化
oread.close()
print(data[1])
