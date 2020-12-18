class Student(object):

    def __init__(self):
        pass
        # self.__name = name
        # self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


s1 = Student()
s1.set_name('ABCD')
s1.set_score(90)
# print(s1.name, s1.name)
s1.print_score()
print(s1.get_name())
print(s1.get_score())


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()
dog.run()
cat.run()


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 25)
print(hasattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z', 404))


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
