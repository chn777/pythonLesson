fs = open("./demo.txt", 'a')

if fs.writable():
    c = fs.write("hello ")
    fs.flush()  # 刷新缓冲区
    print(c)
else:
    print("no")

fs.close()
