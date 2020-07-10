class Animal:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        print("我是%s 我是动物" % self.name)

    def eat(self):
        print("我是%s 吃吃吃,吃东西是我快乐" % self.name)

    def drink(self):
        print("我是%s 喝喝喝,喝饮料是我舒服" % self.name)

    def run(self):
        print("我是%s 跑跑跑,跑步是我健康" % self.name)

    def sleep(self):
        print("我是%s 睡睡睡,睡觉使我得到休息" % self.name)


# 子类拥有父类的所有属性和方法
class Dog(Animal):
    def bark(self):
        print("我是一条狗，我的名字是%s 汪汪汪是我的天性" % self.name)

# # 继承自Animal
# class Cat(Animal):
#     def catch(self):
#         print("我是一只猫，我的名字是%s 抓老鼠是我的本能" % self.name)

# 继承自Dog类
class XiaoTianQuan(Dog):
    def fly(self):
        print("我是一只神犬，我的名字是%s 飞飞飞,飞是我的特性" % self.name)
    def bark(self):
        print("我是神犬，　我的名字是%s　汪汪汪不是我的特性，我还会讲人话" % self.name)

wangcai = XiaoTianQuan("哮天犬")
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
wangcai.fly()

# tom = Cat("汤姆")
# tom.eat()
# tom.drink()
# tom.run()
# tom.sleep()
# tom.catch()
