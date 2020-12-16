# __main__作用于当前py文件，若是被另外的py文件调用，则不会执行属于__main__的语句
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

print('Hello, this is from another file')
