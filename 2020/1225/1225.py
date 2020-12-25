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


# 对10个数进行快速排序。
def question_34(array, left, right):
    if left >= right:
        return
    pivot = array[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= j and array[j] > pivot:
            j -= 1
        while i <= j and array[i] <= pivot:
            i += 1
        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    array[left], array[j] = array[j], array[left]
    question_34(array, left, j - 1)
    question_34(array, j + 1, right)


array = [8, 4, 5, 6, 2, 0, 7, 9, 3, 1]
question_34(array, 0, len(array) - 1)
print('Question 34: ', array)


# 求一个3*3矩阵主对角线元素之和。
def question_35():
    print('Question 35: ')
    a = [[] for n in range(3)]
    a[0] = [1, 2, 3]
    a[1] = [4, 5, 6]
    a[2] = [7, 8, 9]
    for i in range(3):
        for j in range(3):
            print(a[i][j], end='')
        print()

    sum = 0
    for i in range(3):
        sum = sum + a[i][i]

    print('sum = ', sum)


question_35()


# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
def question_36():
    array = [0, 5, 10, 15, 20, 25, 30]
    n = int(input('整数：'))
    array.append(n)
    question_34(array, 0, len(array) - 1)
    print('Question 36: ', array)


question_36()


# 将一个数组逆序输出。
def question_37(array):
    t = array[::-1]
    print('Question 37: ', t)


question_37([1, 2, 3, 4, 5])
