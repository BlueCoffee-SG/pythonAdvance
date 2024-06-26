class Kls1(object):
    bar=1
    def foo(self):
        print('in foo')
    
    #使用类属性，方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)  #类的名字 
        cls().foo()

Kls1.class_foo()

######################
class Story(object):
    snake='Python'
    def __init__(self,name) -> None:
        self.name=name
    #类的方法
    def get_apple_to_eve(cls):
        return cls.snake


s=Story("anyone")
# get_apple_to_eve  是一个bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve, 如果没有，查询story类
print(s.get_apple_to_eve)
#类和实例都可以使用
print(s.get_apple_to_eve())
print(Story.get_apple_to_eve())
print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)


########
class Kls2():
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')


me=Kls2('wilson','yin')
me.print_name()


#输入改为 wilson-yin
'''
解决方法1: 修改__init__()
解决方法2: 增加__new__() 构造函数
解决方法3:增加提前处理的函数
'''


def pre_name(obj,name):
    fname,lname=name.split('-')
    return obj(fname,lname)


me3=pre_name(Kls2,'wilson-yin')
me3.print_name()

#思考  如果用户输入的是"yin,wilson"怎么处理


'''
类方法用在模拟java定义多个构造函数的情况
由于python类中只能有一个初始化方法，不能按不同的情况初始化
'''

class Book(object):
    def __init__(self,title) -> None:
        self.title=title

    @classmethod
    def create(cls,title):
        book=cls(title=title)
        return book
    
book1=Book("python")
book2=Book.create("python and django")



######
class Fruit(object):
    total=0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))


    @classmethod
    def set(cls,value):
        print(f'calling {cls},{value}')
        cls.total=value

'''
    apple.set方法是找的父类方法
'''
class Apple(Fruit):
    pass

class Orang(Fruit):
    pass

Apple.set(100)
#calling <class '__main__.Apple'> ,100

Orang.set(200)
#calling <class '__main__.Orang'> ,200

org=Orang()
org.set(300)
#calling <class '__main__.Orang'> ,300
Apple.print_total() 
 #100
 #1407357110788
 #1407357145788
Orang.print_total()
 #300
 #1407357110788
 #1407357145788