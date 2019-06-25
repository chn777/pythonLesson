# def test():
#     num = 1
#
#     def test2():
#         nonlocal num  # 表示非局部变量
#         num = 9
#         print(num)
#
#     print(num)
#     test2()
#     print(num)
#
#     return test
#
# test()


def test():
    a = 10

    def test2():
        print(a)

    a = 20
    return test2


t = test()
t()
