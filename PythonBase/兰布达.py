# la = lambda x: x * x
# def run(x):
#     return la(x)
#
# print(run(3))


import functools

res = functools.reduce(lambda x ,y :x+y,range(5))
print(res)
gl = globals()

for m in gl:
    print(m)