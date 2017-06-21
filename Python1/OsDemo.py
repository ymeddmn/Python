import os

# encoding=utf-8
# print(os.getcwd())#获取当前脚本的工作目录

# print(os.curdir)  # 返回当前工作目录  .


# print(os.pardir)  # 返回当前父目录字符串名   ..

# os.makedirs("name/haha")  # 生成目录可生成多层
# os.makedirs("../name/haha")  # 在当前目录父目录生成目录可生成多层

# os.mkdir("wowowo")  # 生成单及目录

# os.rmdir("wowowo")  # 删除单及目录，如果不为空不能删除

# os.rename("name", "n")  # 重命名文件

# print(os.stat("n"))  # 获取文件目录信息

# os.system("ls")

# print(os.environ)  # 获取系统环境变量
#
# if os.path.exists('n/sdf.txt'):#判断路径是否存在
#     print('存在')
# else:
#     print('不存在')


print(os.path.getatime('n'))  # 返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime('n'))  # 返回path所指向的文件或者目录的最后修改时间
