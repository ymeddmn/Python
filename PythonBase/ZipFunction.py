# first = ['x','y','z']
# second = ['a','b','c']#输出一个长度的数组
# third = zip(first,second)
# print(third)
#
# for m in third:
#     print(m)


# first = ['x', 'y', 'z']
# second = ['a', 'b']#输出两个长度的数组
# third = zip(first, second)
# print(third)
#
# for m in third:
#     print(m)

def printList(list):
    for j in list:
        print(j)


a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)

printList(c)
d = zip(*c)
printList(d)
