
class MyFirstClass:
    pass


a=MyFirstClass()
b=MyFirstClass()

# 不同的内存地址，两不同对象
type(a)
id(a)
a.__class__()
b.__class__()

#类也是对象
c=MyFirstClass
d=c()
d.__class__()


