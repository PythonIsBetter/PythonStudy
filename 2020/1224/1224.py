# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
def question_17():
    print('Question 17: ')
    for n in range(2, 1000):
        y = []
        for i in range(1, n):
            if n % i == 0:
                y.append(i)
        sum = 0
        for j in y:
            sum = sum + j
        if sum == n:
            print(n)


question_17()


# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def question_18():
    height = 100
    sum = 0
    for n in range(10):
        sum = sum + height
        height = height / 2
        sum = sum + height
    print('Question 18: ', sum, height)


question_18()


# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。
# 求第一天共摘了多少。
def question_19():
    sum = 1
    for n in range(9):
        sum = (sum + 1) * 2
    print('Question 19: ', sum)


question_19()


# 两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。
# 有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
def question_20():
    list_20_a = ['c', 'b', 'a']
    list_20_b = ['x', 'y', 'z']
    print('Question 20: ')
    for a in list_20_a:
        for b in list_20_b:
            if (a == 'c') and (b != 'x') and (b != 'z'):
                print(a, '-', b)
                list_20_a.remove(a)
                list_20_b.remove(b)
            if (a == 'a') and (b != 'x'):
                print(a, '-', b)
                list_20_a.remove(a)
                list_20_b.remove(b)

    for a in list_20_a:
        for b in list_20_b:
            print(a, '-', b)


question_20()


# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
def question_21():
    print('Question 21: ')
    star = 1
    for i in range(1, 5):
        for j in range(1, 5 - i):
            print(' ', end='')
        for k in range(1, star + 1):
            print('*', end='')
        for j in range(1, 4 - i):
            print(' ', end='')
        star += 2
        print()

    star -= 4

    for i in range(4, 1, -1):
        for j in range(1, 6 - i):
            print(' ', end='')
        for k in range(1, star + 1):
            print('*', end='')
        for j in range(1, 4 - i):
            print(' ', end='')
        star -= 2
        print()


question_21()


# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
def question_22():
    a = 2.0
    b = 1.0
    sum = 0
    for i in range(1, 21):
        sum = sum + (a / b)
        t = a
        a = a + b
        b = t
    print('Question 22: ', sum)


question_22()


# 求1+2!+3!+...+20!的和。
def question_23():
    sum = 0
    for i in range(1, 21):
        x = 1
        for j in range(1, i + 1):
            x = x * j
        sum = sum + x
    print('Question 23: ', sum)


question_23()


# 利用递归方法求5!。
def question_24(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n * question_24(n - 1)
    return sum


print('Question 24: ', question_24(5))


# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def question_25(s, length):
    if length == 0:
        return
    print(s[length - 1], end='')
    question_25(s, length - 1)


print('Question 25: ', end='')
question_25('abcde', 5)
print()


# 有5个人坐在一起，
# 问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。
# 请问第五个人多大？
def question_26(n):
    if n == 1:
        return 10
    else:
        return 2 + question_26(n - 1)


print('Question 26: ', question_26(5))


# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def question_27():
    print('Question 27: ', end='')
    n = 12345
    a = n // 10000
    b = n % 10000 // 1000
    c = n % 1000 // 100
    d = n % 100 // 10
    e = n % 10
    if a != 0:
        print(5, '位数：', e, d, c, b, a)
    elif b != 0:
        print(4, '位数：', e, d, c, b)
    elif c != 0:
        print(3, '位数：', e, d, c)
    elif d != 0:
        print(2, '位数：', e, d)
    elif e != 0:
        print(1, '位数：', e)


question_27()


# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
def question_28():
    n = int(input('整数'))
    a = n // 10000
    b = n % 10000 // 1000
    c = n % 1000 // 100
    d = n % 100 // 10
    e = n % 10
    print('Question 28: ', end='')
    if a == e and b == d:
        print('Yes')
    else:
        print('No')


question_28()


# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
def question_29():
    print('Question 29: ')
    letter = input("please input:")
    # while letter  != 'Y':
    if letter == 'S':
        print('please input second letter:')
        letter = input("please input:")
        if letter == 'a':
            print('Saturday')
        elif letter == 'u':
            print('Sunday')
        else:
            print('data error')

    elif letter == 'F':
        print('Friday')

    elif letter == 'M':
        print('Monday')

    elif letter == 'T':
        print('please input second letter')
        letter = input("please input:")

        if letter == 'u':
            print('Tuesday')
        elif letter == 'h':
            print('Thursday')
        else:
            print('data error')

    elif letter == 'W':
        print('Wednesday')
    else:
        print('data error')


question_29()


# 按相反的顺序输出列表的值。
def question_30():
    list_30 = ['Hello', 'World', '!']
    print('Question 30: ', list_30[::-1])


question_30()


# 按逗号分隔列表。
def question_31():
    list_31 = [1, 2, 3, 4, 5]
    print('Question 31: ', list_31[0], end='')
    for n in list_31[1:]:
        print(',', n, end='')
    print()


question_31()


# 文本颜色设置。
# class question_32:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
#
# print('Question 32: ', question_32.WARNING + "警告的颜色字体?")


# 求100之内的素数。
def question_33():
    result = []
    for n in range(2, 101):
        for j in range(2, n):
            if n % j == 0:
                break
        else:
            result.append(n)
    print('Question 33: ', result)


question_33()
