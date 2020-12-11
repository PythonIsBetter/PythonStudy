x = 20
if x:
    print('True')

# birth = int(input('birth: '))
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


#  red  green  blue  yellow  white  black
#  0    1      2     3       4      5
# -6   -5     -4    -3      -2     -1
list_4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list_4[0], list_4[1], list_4[2])
print(list_4[-1], list_4[-2], list_4[-3])
print(list_4[0: 3], list_4[0: -3])

del list_4[-1]
print(list_4)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print(len(list_1))
print(list_1 + list_2)
print(list_1 * 2)
# print(list_1 ** 2)
print(3 in list_1)

list_3 = [list_1, list_2]
print(list_3)
print(list_3[0], list_3[1])
print(list_3[0][2])

# 默认移除最右边的元素
# 可以指定list的序号
list_1.pop(1)
print(list_1)

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

# 与
c = a & b  # 12 = 0000 1100
print("a & b：", c)

# 或
c = a | b  # 61 = 0011 1101
print("a | b：", c)

# 异或
c = a ^ b  # 49 = 0011 0001
print("a ^ b：", c)

# 每一位取反码，得到补码
c = ~a  # -61 = 1100 0011
print("~a：", c)

# 左移
c = a << 2  # 240 = 1111 0000
print("a << 2：", c)

# 右移
c = a >> 2  # 15 = 0000 1111
print("a >> 2：", c)

L = list(range(1, 11))
print(L)
L = [x * x for x in range(1, 10)]
print(L)
L = [x for x in range(1, 20) if x % 2 == 0]
print(L)
L = [x + y for x in 'ABC' for y in 'DEF']
print(L)
L = [x + y + z for x in 'AB' for y in 'CD' for z in 'EF']
print(L)
L = [x + y for x in 'AB' for y in 'CDEF']
print(L)
L = [x if x % 2 == 0 else -x for x in range(1, 10)]
print(L)
L = [x if x % 2 != 0 else -x for x in range(1, 10)]
print(L)


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
