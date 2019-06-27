def test():
    res1 = yield 1
    print(res1)

    res2 = yield 2
    print(res2)


g = test()
print(g.__next__())
print(g.send("he"))
