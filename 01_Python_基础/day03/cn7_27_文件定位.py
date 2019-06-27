

# 打开文件
fs = open('./demo.txt', 'r')


# 读写操作
print(fs.tell())
fs.seek(3)
print(fs.tell())
content = fs.read()
print(content)


# 关闭文件
fs.close()
