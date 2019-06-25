# 当一个函数A的参数，接收的是另一个函数时，则函数A就是高阶函数


def fn1(num1, num2):
    return num1 + num2


def fn2(num1, num2):
    return num1 - num2


def test(num1, num2, fn):
    print(fn(num1, num2))


test(5, 6, fn1)
test(5, 6, fn2)
