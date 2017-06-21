import time

# a = time.clock()  # 返回处理器的时间，float类型
# print(a)

# print(time.altzone)  # 返回与utc时间的时间差

# print(time.asctime())#返回时间格式"Fri Aug 19 11:14:16 2016",

# print(time.localtime())#返回本地时间的格式#


# a = time.strptime('2017/3/9', '%Y/%m/%d')  # 将时间转换为struct结构对象
# print(a)
#
# b = time.mktime(a)#将struct时间对象转换为时间戳
# print(b)





import datetime

# print(datetime.datetime.now())#返回当前时间

# print(datetime.date.fromtimestamp(time.time()))#将时间戳转换为时间格式


# print(datetime.datetime.now() + datetime.timedelta(days=5))  # 当前时间加五天
#
# print(datetime.datetime.now() + datetime.timedelta(hours=5))  # 当前时间加五小时




# t = datetime.datetime.now()
# print(t)
# print(t.replace(hour=21, minute=50, second=20))  # 时间替换



