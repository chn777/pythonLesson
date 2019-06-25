# d = dict.fromkeys("abc")
d = dict.fromkeys(["name", "age"], "chn777")
print(d)


# 只能改变字典键值对的值，而非键
person = {"name": "CH777", "Age": 28}
# []方式
print(person)
person["Age"] = 29
print(person)

person_new = {"name": "Jiang", "Age": 29, "Location": "BJ"}

res = person.update(person_new)
print(res)
print(person)
print(person_new)

for key in person.keys():
    print(key, ":", person[key])

for k, v in person.items():
    print(v)

for item in person.items():
    print(item[0], "-->", item[1])

