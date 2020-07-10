class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test(self):
        print("公有方法　%d %d" % (self.num1,self.__num2))

    def __test(self):
        print("私有方法　%d %d" % (self.num1, self.__num2))


# 子类对象不能直接访问父类的私有属性和私有方法
class B(A):

    def demo(self):

        # 1.访问父类的私有属性,在子类对象的方法中不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        pass
        # 2. 调用父类的私有方法，在子类对象的方法中不能调用父类的私有方法
        # self.__test()

# 创建一个子类对象
b = B()
print(b.num1)
b.test()

b.demo()

# # 在外界不能访问私有属性和私有方法
# print(b.num1)
# print(b._A__num2)
