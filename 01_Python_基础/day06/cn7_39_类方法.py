class Person:
    __slots__ = ["age", "num", "name"]

    # 类方法
    @classmethod
    def leifangfa(cls, k):
        print("类方法", cls, k)

    pass


Person.leifangfa("123")

p1 = Person()
p1.leifangfa(k=999)


