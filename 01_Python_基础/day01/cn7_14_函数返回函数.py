# 一个函数作为另一个函数的返回值

def sumfn(a, b, c):
    return a + b + c


def jianfn(a, b, c):
    return a - b - c


def test_fun(flag):
    if flag == "+":
        return sumfn
    elif flag == "-":
        return jianfn


res = test_fun("+")
# res = test_fun("-")
print(res)
print(type(res))
print(res(1, 2, 3))

