
# 定义列表
# lis = [i for i in range(1, 100) if i % 2 == 0]
# print(lis)

# 生成器定义1
"""
gn = (i for i in range(1, 100) if i % 2 == 0)
print(gn)
print(next(gn))
print(gn.__next__())

for i in gn:
    print('for--', i)
"""


# 生成器定义2
# yield 相当于一个断点，使用next函数，可以让当前函数执行到yield语句为止，同时返回yield的状态值
# def test():
#     print('hello1')
#     yield "statusV1"
#
#     print("hello2")
#     yield "statusV2"
#
#     print("hello3")
#     yield "statusV3"

def test():
    for i in range(1, 9):
        print("hello", i)
        yield "statusValue " + str(i)


g = test()
print(g.__next__())
s2 = next(g)
print(s2)
