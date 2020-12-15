def person1(name, age, **kw):
    print(name, age, kw)


person1('A', 5, b='A')

list1 = {'a': 'A', 'b': 'B', 'c': 'C'}
person1('B', 10, **list1)


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('C', 20, city='T', job='E')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)


def add(x, y, f):
    return f(x) + f(y)


print(add(-6, -7, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])  # map的作用相当于是把函数作用到了后续的list里
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5])))

from functools import reduce


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))  # reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def prod(L):
    def ji(x, y):
        return x * y

    return reduce(ji, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# s = '12.34'
# print(len(s))
# print(s.find('.'))
# print(len(s) - s.find('.') - 1)


def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    if ('.' in s):
        index = s.find('.')
        return reduce(fn, map(char2num, s[:index] + s[index + 1:])) / (10 ** (len(s) - index - 1))
    else:
        return reduce(fn, map(char2num, s))


print('str2float(\'123.456\') =', str2float('123.456'))


def createCounter():
    L1 = []

    def count():
        L1.append(0)
        return len(L1)

    return count


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
