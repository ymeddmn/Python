# coding=gbk

info = {
    1: '1',
    2: '1'
}

# o = open('a.text', 'w')
# o.write(str(info))  # д�ļ�
# o.close()


oread = open('a.text', 'r')
data = eval(oread.read())  # ���ļ���eval�Ƿ����л�
oread.close()
print(data[1])
