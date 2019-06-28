class Person:
    """
        是一个类
    """

    # 添加类属性 方法一
    dis = "描述"

    pass


# 添加类属性 方法二
Person.name = "人类"

print(Person.dis)
print(Person.name)
print(Person.__dict__)
print(Person.__doc__)

p = Person()
# 类属性可以通过对象来访问，类属性会被各个对象所共享
p.dis = "s"
p.age = 12
print(p.dis)
print(p.name)


