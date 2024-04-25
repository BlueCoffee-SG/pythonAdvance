# 钻石继承

class BaseClass(object):
    num_base_calls=0
    def call_me(self):
        print('call method on base `Class`')
        self.num_base_calls+=1


class LeftSubclass(BaseClass):
    num_left_calls=0
    def call_me(self):
        print('call method on left  Subclass')
        self.num_left_calls+=1
    
class RightSubclass(object):
    num_right_calls=0
    def call_me(self):
        print('call method on Right Subclass')
        self.num_right_calls+=1

class Subclass(LeftSubclass,RightSubclass):
    pass

a=Subclass()
a.call_me()


print(Subclass.mro())
# 广度优先，另外python3 中不加(obj ect)也是新式类，但是为了代码不会误运行在python2下产生意外结果 ，建议增加
# >>> Subclass.mro()
# [<class '__main__.Subclass'>,<class '__main__.leftSubclass'>, <class '__main__.RightSubclass'>,<class '__main__'>]


#修改RightSubclass的父类 object
# >>> Subclass.mro()
# [<class '__main__.Subclass'>,<class '__main__.leftSubclass'>, <class '__main__.BaseC lass'>,<class '__main__'>]