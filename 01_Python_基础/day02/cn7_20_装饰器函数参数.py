def zsq(func):
    def inner(*args, **kwargs):
        print("-" * 10)
        func(*args, **kwargs)
    return inner


@zsq
def test(n):
    print(n)


@zsq
def test2(n, m, x):
    print(n, m, x)


test(1)

test2(1, 2, x=7)
