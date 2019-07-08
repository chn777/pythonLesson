class Person:
    __slots__ = ["age", "num", "name"]

    # 实例方法
    def say(self):
        print(self.name, self)

    # 类方法
    @classmethod
    def leifangfa(cls):
        print('classmethod', cls)

    # 静态方法
    @staticmethod
    def jtff():
        print('staticmethod')

    pass


p1 = Person()
p1.name = "Python"

# 调用实例方法
p1.say()

# 调用类方法
p1.leifangfa()
Person.leifangfa()

# 静态方法
p1.jtff()
Person.jtff()


