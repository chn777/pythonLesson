class Person:
    __slots__ = ["age", "num"]
    pass


p1 = Person()

p1.age = 123

print(p1)

