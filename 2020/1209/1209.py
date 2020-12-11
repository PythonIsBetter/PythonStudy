print(ord('a'))

print(ord('日'))
print(ord('本'))

a1 = hex(ord('日'))
a2 = hex(ord('本'))

print(a1, a2)

b = chr(44)
print(b)

print('\u65e5\u672c')

print('日本'.encode('UTF-8'))  # 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print('日本'.encode('Shift_JIS'))

print(b'\xe6\x97\xa3'.decode('UTF-8'))

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('%4d-%03d' % (3, 1))
print('%.4f' % 3.1415926)  # 会自动四舍五入
print('%02d%%' % 5)

print('This {0} a {1}:{2: .3f}'.format('is', 'num\\ber', 1.54874557))

# not > and > or
x = True
y = False
z = False

print(not x or y or not y and x)

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

#  H  e  l  l  o
#  0  1  2  3  4
# -5 -4 -3 -2 -1
a = "Hello"
b = "Python"

print('a[:]', a[:])
print('a[1:]', a[1:])
print('a[-1]', a[-1])
print('a[-1:]', a[-1:])
print('a[:-1]', a[:-1])
print('a[:0]', a[:0])
print('a[-5:]', a[-5:])
print('a[:-5]', a[:-5])
print('a[1000:]', a[1000:])
print('a[:1000]', a[:1000])
print('a[-1000:]', a[-1000:])
print('a[:-1000]', a[:-1000])


print("a + b：", a + b)
print("a * 2：", a * 2)
print("a[1]：", a[1])
print("a[1:4]：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')
