# 直接在函数体的上方用三个双引号对注释
def my_fn(num1, num2=1):
    """
    计算两个数的和
    :param num1: 数值1，数值类型，不可选，没有默认值
    :param num2: 数值2，数值类型，可选，默认值1
    :return: 返回计算的结果，数值类型
    """
    return num1 + num2


help(my_fn)
print(my_fn(1))
