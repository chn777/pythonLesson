class Person:
    __slots__ = ["age", "num", "name"]

    # 静态
    @staticmethod
    def jtff():
        print("静态方法")

    pass


Person.jtff()
p = Person()
p.jtff()


