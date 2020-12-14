tup1 = (1, 2, 3, 4, 5, 6, 7)
print(tup1)

tup2 = (50)
tup3 = (50,)
print((type(tup2)))
print((type(tup3)))

print(tup1[1:])
print(tup1[1:-2])

# tup1[0]=2
# print(tup1)

# del(tup2)
# print(tup2)

print(len(tup3))
print(tup3 + tup1)
print(tup3 * 5)
print(3 in tup1)

list1 = [1, 2, 3, 4, 5]
tup4 = tuple(list1)
print(tup4)

dict1 = {'a': 'A', 'b': 'U', 'c': 'C', 'd': 'D', 'e': 'E'}
print(dict1['a'])
dict1['f'] = 'F'
dict1['b'] = 'B'
print(dict1)

# 如果同一个键被赋值两次，后一个值会被记住
dict2 = {'a': 1, 'b': 2, 'a': 3}
print(dict2)
print(dict2['a'])

print(dict1)
print(str(dict1))

print(dict1.popitem())
print(dict1)

import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# 默认参数不能指向对象
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end(['a', 'b', 'c']))
print(add_end())
print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


print(calc(1, 2, 3, 4))
print(calc(2, 5))
print(calc())


def product(x, *number):
    sum = x
    for n in number:
        sum *= n
    return sum


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
