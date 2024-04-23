# 父类
class People(object):
    def __init__(self) -> None:
        self.gene="XY"
    
    def walk(self):
        print("I can walk")

# 子类
class Man(People):
    def __init__(self,name) -> None:
        self.name=name

    def work(self):
        print('work hard')



class Woman(People):
    def __init__(self,name) -> None:
        self.name=name

    def shopping(self):
        print('buy buy buy')

p1=Man('Adam')
p2=Woman('Eve')

# 问题1 gene有没有被继承
p1.gene (不能，init方法覆盖了)

# 问题2 People的父类是谁
object ,object父类中空的

#问题3 能否实现多重层级继承
可以 
#问题4 能否实现多个父类同时继承
可以



################
class People(object):
    def __init__(self,name) -> None:
        self.gene="XY"
        # 假设人人都有名字
        self.name=name 
    
    def walk(self):
        print("I can walk")


# 子类
class Man(People):
    def __init__(self,name) -> None:
        #把到 Man的父类people ,把类People的对象转成为类Man的对象
        super().__init__(name)

    def work(self):
        print('work hard')



class Woman(People):
    def __init__(self,name) -> None:
        super().__init__(name)


p1=Man('Adam')
p2=Woman('Eve')

# 问题1 gene有没有被继承
# super(Man,self).__init__()
p1.gene 

# 问题2 People的父类是谁
#object 与type
print('object',object.__class__,object.__bases__)
print('type',type.__class__,type.__bases__)
#type元类由type自身创建，object类由元类type创建
# type类继承了object类


#问题4 能否实现多个父类同时继承
class Son(Man,Woman):
    pass
#新的问题： 继承的顺序
# 钻石继承