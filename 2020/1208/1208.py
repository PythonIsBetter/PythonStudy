print(r'''hello,\n
world''')
print(r'''hello
,
world
!''')
print(r'hello \n world')
print('hello \nworld')
print('\\hello \\\nworld\t!')
print('hello "world"')

# name = input()
# print('hello world', name)
# name = input('input your name plz: ')
# print('hello world', name)

a, b, c = 21, 10, 0

c = a + b
print("a + b：", c)

c = a - b
print("a - b：", c)

c = a * b
print("a * b：", c)

c = a / b
print("a / b：", c)

c = a % b  # 取模 - 返回除法的余数
print("a % b：", c)

c = a ** b  # 幂 - 返回x的y次幂
print("a ** b：", c)

c = a // b  # 取整除 - 向下取接近商的整数
print("a // b：", c)

# 海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符
# 在这个示例中，赋值表达式可以避免调用 len() 两次
a = 'Hello World'
if (n := len(a)) > 1:
    print(f"List is too long ({n} elements)")


