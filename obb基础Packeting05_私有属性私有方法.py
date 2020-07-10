class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象方法的内部可以访问私有属性
        print("%s 的年龄是 %d" % (self.name, self.__age))


# 私有属性，不能被直接在外界访问
xiaofang = Women("小芳")
# print(xiaofang.__age)
# 私有方法，同样不能被直接在外界访问
# xiaofang.secret()

# python 中的私有属性，私有方法为伪私有
# 外界调用私有属性和私有方法
# 处理方式：在名称前面加上_类名
print(xiaofang._Women__age)
print(xiaofang._Women__secret())