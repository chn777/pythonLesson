fs = open('./demo.txt', 'r')

# print(fs.read(3))
#
# print(fs.readline())

# ls = fs.readlines()

# print(ls[0])
#
# for i in ls:
#     print(i, end="")

print(fs.readable())

if fs.readable():
    print(1)
else:
    print("no")

fs.close()
