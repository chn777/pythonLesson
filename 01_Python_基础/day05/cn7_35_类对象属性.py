class Person:
    """
        是一个类
    """
    pass


p = Person()
# 动态添加属性
p.name = "zhangs"
p.height = 180

print(p.name)
print(p.__dict__)
print(p.__doc__)

# 删除对象属性
del p.name

print(p.__dict__)
