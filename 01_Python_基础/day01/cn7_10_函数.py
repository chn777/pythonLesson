# 1、无参数 无返回值函数的定义
# def tell():
#     print("hello")
#
#
# tell()


# 2、定义一个参数的函数
# def test(num):
#     print(num ** 3)
#
#
# test(2)


# 3、定义多个参数
# def mysum(num1, num2):
#     print("num2", num2)
#     print(num1 + num2)
#
#
# mysum(1, 3)
# mysum(num2=2, num1=5)

# 4、定义不定长参数函数
# 方式1、方法名(*参数) 该参数就是一个元组类型的参数
# def mysum2(*tuplev):
#     print(type(tuplev))
#     res = 0
#     for v in tuplev:
#         res += v
#     print(res)
#
#
# mysum2(1, 2, 3, 4)


# 方式2、(**参数) 该参数就是一个字典类型的参数
# def mysum3(**numbs):
#     print(numbs, type(numbs))
#
#
# mysum3(k1="hello", k2=12, name="hello")

# 装包与拆包
# def my_sum(a, b):
#     print(a + b)


# def test(*args):
#     print(args)
# 拆包
# print(*args)
# my_sum(*args)


# def test2(**kwargs):
#     print(kwargs)
# 拆包
# my_sum(**kwargs)


# test(1, 2)
# test2(a=5, b=6)
