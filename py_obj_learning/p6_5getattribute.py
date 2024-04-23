
class Human2(object):

    def __init__(self) -> None:
        self.age=10


    def __getattr__(self,item):
        #对指定属性做处理，fly属性返回'superman',其它属性返回NOne
        self.item=item
        if self.item=='fly':
            return 'superman'
    
h1=Human2()

print(h1.age)
print(h1.fly)
print(h1.noattr)