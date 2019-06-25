def check_login(func):
    def inner():
        print("登录验证")
        func()
    return inner


def fss():
    print("发说说")


fss = check_login(fss)


def ftp():
    print("发图片")


ftp = check_login(ftp)


buttonIndex = 2
if buttonIndex == 1:
    fss()
else:
    ftp()
