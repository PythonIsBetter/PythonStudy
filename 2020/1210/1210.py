n, sum = 100, 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

count = 1
while count < 3:
    print(count, "<3")
    count = count + 1
else:
    print(count, "=3")

for i in range(3):
    print(i)

for i in range(10, 13):
    print(i)

# 开始 结束 步长
for i in range(20, 30, 3):
    print(i)

a = ['A', 'B', 'C']
for i in range(len(a)):
    print('%s %s' % (i, a[i]))

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

d = ['a', 'b', 'c']
for i, v in enumerate(d):
    print(i, v)


def fun(L):
    if (len(L) == 0):
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if (i < min):
            min = i
        if (i > max):
            max = i
    return (min, max)


print(fun([6, 8, 4, 10, 7, 1]))
