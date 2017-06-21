# def createGenerator():
#     myList = range(5);
#     for i in myList:
#         yield i*i
#
# myGen = createGenerator()
# for m in myGen:
#     print(m)

# yield 返回的必须是一个生成器



def consumer():
    print('准备吃包子')
    while True:
        baozi = yield
        print('包子的name', baozi)

c = consumer()
c.__next__()
c.send('j')  # 给consumer传值

