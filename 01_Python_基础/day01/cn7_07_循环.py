# while 单循环
rg = 30
while rg < 100:
    if rg == 50:
        rg += 20
        # continue
        break
    else:
        print(rg)
        rg += 20


# while else 循环
i = 7
while i < 10:
    print(i)
    i += 1
else:
    print("over")


# for 循环
dArr = ["hello", "world"]
for x in dArr:
    print(x)

# for else 循环
for i in dArr:
    print(i)
else:
    print("over")


