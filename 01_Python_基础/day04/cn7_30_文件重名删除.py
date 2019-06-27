
import os

# 不仅可以重命名文件，也可以重命名文件夹
# os.rename('demo1.txt', 'demo.txt')
# os.rename('o', 'newDir')

# 多层重命名
# os.renames("dir/hello/conf.ini", "newDir/file.txt")

# os.remove("co.png")
# os.removedirs('newDir/d2')  # 递归删除
os.rmdir("newDir/d2")       # 非递归删除
