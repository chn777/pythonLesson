def get_zsq(char):
    def zsq(func):
        def inner():
            print(char * 20)
            func()
        return inner
    return zsq


@get_zsq("&")
def test():
    print("hello")


test()
