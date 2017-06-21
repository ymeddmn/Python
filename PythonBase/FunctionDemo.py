# 函数讲解

# def mage():
#     print('打印')
# mage()



# def returnData(n):
#     if (n > 5):
#         return '有点短小'
#     else:
#         return '还行'
#
# strs = returnData(4)
# print(strs)



# def returnInt(n=34):#函数默认值
#     return n;
#
# mn = returnInt(4);
# mn1 = returnInt();
# print(mn)
# print(mn1)




# def printData(x='3', y='4', z=4):
#     print(x, y, z)
#
# printData()
# printData('44', 'sdf', 2)
# printData(y='马哥')


def printArg(*args):#python可变参数
    for n in args:
        print(n)

printArg(2,3,4,4,5)