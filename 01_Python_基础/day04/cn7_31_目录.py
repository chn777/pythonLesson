import os

# 获取当前目录
print('c', os.getcwd())

# 改变默认目录
os.chdir('a')

# 获取目录内容
print('ct', os.listdir(os.getcwd()))








