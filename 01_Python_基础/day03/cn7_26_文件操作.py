

# 打开文件
fs = open('./tp.png', 'rb')
fs2 = open('./co.png', 'wb')
"""
    r 只读          文件指针指向文件开头0位置 文件不存在会报错
    w 只写          文件指向指向0位置，文件不存在，会创建新文件
    a 只写（追加）   文件指向指向文件末尾位置，文件不存在，会创建新文件
    b 组合          二进制文件操作 rb,wb,ab
    + 组合          改为读写操作 r+ w+ a+ rb+ wb+ ab+
"""

# 读写操作
# content = fs.read()
# print(content)
content = fs.read()
jpg = content[0: len(content) // 2]
fs2.write(jpg)

# 关闭文件
fs.close()
fs2.close()
