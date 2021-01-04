import random


# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
def question_38():
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            result[i][j] = X[i][j] + Y[i][j]

    print('Question 38: ', result)


question_38()


# 统计 1 到 100 之和。
def question_39():
    sum = 0
    for i in range(101):
        sum += i
    print('Question 39: ', sum)


question_39()


# 求输入数字的平方，如果平方运算后小于 50 则退出。
def question_40():
    print('Question 40: ')
    while True:
        num = int(input('整数：'))
        s = num ** 2
        print('%d 的平方：%d' % (num, s))
        if s < 50:
            break


# question_40()


# 两个变量值互换。
def question_41():
    print('Question 41: ')
    a = int(input('整数：'))
    b = int(input('整数：'))
    t = a
    a = b
    b = t
    print('%d %d' % (a, b))


# question_41()


# 数字比较。
def question_42():
    list_42 = []
    while True:
        num = int(input('整数：'))
        list_42.append(num)
        if num >= 100:
            break
    list_42.sort()
    print('Question 42: ', list_42)


# question_42()


# 使用lambda来创建匿名函数。
def question_43():
    a = 10
    b = 20
    MAX = lambda x, y: (x > y) * x + (x < y) * y
    MIN = lambda x, y: (x > y) * y + (x < y) * x
    print('Question 43: 最大值--%d 最小值--%d' % (MAX(a, b), MIN(a, b)))


question_43()


# 输出一个随机数。
def question_44():
    print('Question 43: 随机数', random.uniform(0, 100))


question_44()


# 学习使用按位与 & 。
def question_45():
    print('Question 45: ')
    a = 0x23
    print(bin(a), bin(3))
    b = a & 3
    print(b)
    print(bin(b))
    b = b & 4
    print(b)
    print(bin(b))


question_45()


# 学习使用按位或 | 。
def question_46():
    print('Question 46: ')
    a = 0x10
    print(bin(a), bin(0xf))
    b = a | 0xf
    print(b)
    print(bin(b))
    b = b | 0
    print(b)
    print(bin(b))


question_46()


# 学习使用按位异或 ^ 。
def question_47():
    print('Question 47: ')
    a = 0o77
    print(bin(a), bin(3))
    b = a ^ 3
    print(b)
    print(bin(b))
    b = b ^ 7
    print(b)
    print(bin(b))


question_47()


# 取一个整数a从右端开始的4〜7位。
def question_48():
    a = 16
    a = a >> 4
    b = 0
    b = ~(~0 << 4)
    print('Question 48: ', a & b)


question_48()


# 学习使用按位取反~。
def question_49():
    a = 7
    b = ~a
    c = -7
    d = ~c
    print('Question 49: ', b, d)


question_49()


# 计算字符串长度。
def question_50():
    string = 'abcdefg'
    print('Question 50: ', len(string))


question_50()
