a = {3: 3, 2: 4, 1: 0, 9: 1, 2: 1}
print(a)  # 无序的打印

print(sorted(a.items()))  # 对a进行排序，根据key排序

print(sorted(a.items(), key=lambda x: x[1]))#按照value排序





