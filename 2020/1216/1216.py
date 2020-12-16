import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\nPython 路径为：', sys.path, '\n')

import supertest

print(dir(supertest))
print(dir(sys))


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
