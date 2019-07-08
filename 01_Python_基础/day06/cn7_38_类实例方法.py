class Person:
    __slots__ = ["age", "num", "name"]

    # 实例方法
    def say(self, tag):
        print(tag)

    pass


p1 = Person()
p1.say(tag="Python")

Person.say(p1, "Python Class1")

Person.say(p1, tag="Python Class2")


