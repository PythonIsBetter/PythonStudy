import sys

print(sys.platform)

assert ('win32' in sys.platform), "该代码只能在 Linux 下执行"

try:
    x = int(input('输入一个整数：'))
except ValueError:
    print('非法输入')
else:
    print('这是整数')
finally:
    print('完成输入')

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print('111')


# x = 10
x=4
if x > 5:
    raise Exception('x不能大于5\nx的值为:%d' % x)

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


foo('0')


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 60 <= self.score < 80:
            return 'B'
        elif 80 <= self.score < 100:
            return 'A'
        elif self.score < 0 or self.score > 100:
            raise ValueError
        return 'C'


def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    -1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
