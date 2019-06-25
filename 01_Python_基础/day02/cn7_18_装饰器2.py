def check_login(func):
    print("开始执行")

    def inner():
        print("验证")
        func()
    return inner


@check_login  # 等价于 fss = check_login(fss)
def fss():
    print("发说说")


# fss()
