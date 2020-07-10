class Tool(object):

    # 使用赋值语句定义类属性，　记录所有工具对象的数量
     count = 0

     def __init__(self, name):
         self.name = name

         # 让类属性的值+1
         Tool.count += 1

# 定义类属性：给类对象中定义的属性，通常记录与这个类相关的特征
# 类属性不会用于记录具体对象的特征


# 1. 创建工具对象

tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("水桶")

tool3.count = 99
# 2. 输出工具对象的总数
print("工具对象总数　%d" % tool3.count)
print(Tool.count)