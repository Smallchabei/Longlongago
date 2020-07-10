class A:

    def test(self):
        print("A-----test 方法")

    def demo(self):
        print("A-----demo方法")


class B:

    def test(self):
        print("B-----test方法")

    def demo(self):
        print("B-----demo　方法")


class C(B,A):
    pass

# 多继承
# 创建子类对象
# 重名时会调用按顺序调用各个父类中的属性和方法
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

c = C()

c.test()
c.demo()

# C类对象调用方法的顺序
print(C.__mro__)