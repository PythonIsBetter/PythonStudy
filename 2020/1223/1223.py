import math, time, string


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def question_1():
    list_1 = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    list_1.append(i * 100 + j * 10 + k)
    print('Question 1: ', list_1)


question_1()


# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
def question_2():
    # i = int(input('利润：'))
    i = 1200000
    i = i / 100000
    arr = [10, 6, 4, 2, 1, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for n in range(len(arr)):
        if (i > arr[n]):
            x = (i - arr[n]) * rate[n]
            r = r + x
            i = arr[n]
    print('Question 2: ', r * 100000)


question_2()


# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def question_3():
    list_3 = []
    result = []
    while True:
        i = len(list_3)
        a = i + 100
        b = a + 168
        a_1 = int(math.sqrt(a))
        b_1 = int(math.sqrt(b))
        if (a_1 ** 2 == a) and (b_1 ** 2 == b):
            result.append(i)
        list_3.append(1)
        if (len(list_3) >= 10000):
            break

    list_3 = []
    while True:
        i = 0 - len(list_3)
        a = i + 100
        b = a + 168
        if a > 0 and b > 0:
            a_1 = int(math.sqrt(a))
            b_1 = int(math.sqrt(b))
            if (a_1 ** 2 == a) and (b_1 ** 2 == b):
                result.append(i)
        if (len(list_3) >= 10000):
            break
        list_3.append(1)

    print('Question 3: ', result)


question_3()


# 输入某年某月某日，判断这一天是这一年的第几天？
def question_4():
    # date = str(input('YYYYMMDD：'))
    date = '20201223'
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    days = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and (month >= 3):
        print('Question 4: ', days[month - 1] + day + 1)
    else:
        print('Question 4: ', days[month - 1] + day)


question_4()


# 输入三个整数x,y,z，请把这三个数由小到大输出。
def question_5():
    list_5 = [10, 20, 30]
    # for n in range(3):
    #     list_5.append(int(input('整数：')))
    list_5.sort()
    print('Question 5: ', list_5)


question_5()


# 斐波那契数列
def question_6():
    # n = int(input('整数：'))
    n = 10
    list_6 = [0, 1]

    if n == 1:
        print('Question 6: ', list_6[0])
        return
    if n == 2:
        print('Question 6: ', list_6)
        return
    else:
        for i in range(2, n):
            list_6.append(list_6[i - 2] + list_6[i - 1])
        print('Question 6: ', list_6)
        return


question_6()


# 输出 9*9 乘法口诀表。
def question_7():
    print('Question 7:')
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end=' ')
        print()


question_7()


# 暂停一秒输出。
def question_8():
    print('Question 8:')
    list_8 = ['Hello', 'World']
    for n in range(len(list_8)):
        print(list_8[n])
        time.sleep(1)


question_8()


# 暂停一秒输出，并格式化当前时间。
def question_9():
    print('Question 9:')
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


question_9()


# 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
def question_10():
    n = int(input('整数：'))

    list_10 = [2, 2]

    if n < 3:
        print('Question 10: ', 2)
        return
    else:
        for i in range(2, n):
            list_10.append(list_10[i - 2] + list_10[i - 1])
        print('Question 10: ', list_10)
        return


question_10()


# 判断101-200之间有多少个素数，并输出所有素数。
def question_11():
    result = []
    for n in range(101, 200):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            result.append(n)
    print('Question 11: Total - ', len(result))
    print(result)


question_11()


# 打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
def question_12():
    result = []
    for n in range(100, 1000):
        a, b, c = n // 100, n // 10 % 10, n % 10
        if a ** 3 + b ** 3 + c ** 3 == n:
            result.append(n)
    print('Question 12: ', result)


question_12()


# 将一个正整数分解质因数。
def question_13():
    n = int(input('整数：'))
    print('Question 13: ')
    while n not in [1]:
        for index in range(2, n + 1):
            if n % index == 0:
                n = n // index
                if n == 1:
                    print(index)
                else:
                    print('{} *'.format(index), end=" ")
                break


question_13()


# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
def question_14(score):
    if score >= 90:
        grade = 'A'
    elif 60 <= score < 90:
        grade = 'B'
    else:
        grade = 'C'
    print('Question 14: ', grade)


question_14(100)


# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
def question_15():
    s = input('字符串：')
    letter, number, space, other = 0, 0, 0, 0
    for n in s:
        if n.isalpha():
            letter += 1
        elif n.isdigit():
            number += 1
        elif n.isspace():
            space += 1
        else:
            other += 1
    print('Question 15: 英文字母：%d，空格：%d，数字：%d，其他：%d' % (letter, space, number, other))


question_15()


# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
def question_16():
    a = int(input('数字：'))
    n = int(input('做几次：'))
    sum = 0
    T = 0
    print('Question 16: ')
    for i in range(n):
        T = T * 10 + a
        print(T)
        sum = sum + T
    print(sum)


question_16()
