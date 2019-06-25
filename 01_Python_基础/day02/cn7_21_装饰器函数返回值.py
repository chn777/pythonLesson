def zsq(func):
    def inner(*args, **kwargs):
        print("-" * 10)
        return func(*args, **kwargs)
    return inner


@zsq
def test2(n, m):
    print(n, m)
    return n + m


res = test2(1, 2)
print(res)
