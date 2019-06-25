def zsq1(func):
    print(1)
    def inner():
        print("-"*20)
        func()
    return inner


def zsq2(func):
    print(2)
    def inner():
        print("*" * 20)
        func()
    return inner


@zsq1
@zsq2
def test():
    print("hello")


test()


# 装饰器
# 从上到下装饰
# 从下往上执行
