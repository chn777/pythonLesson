def fn1():
    a = 10

    def fn2():
        print(a)

    return fn2


test = fn1()
test()


def line_config(content, length):

    def print_line():
        print("-" * (length // 2) + content + "-" * (length // 2))

    return print_line


p = line_config('xx', 10)
p()
p()
p()
