# __getattirbute__的底层原理是描述符
from typing import Any


class Desc(object):
    ''''
    通过打印来展示描述器的访问流程
    '''

    def __init__(self,name) -> None:
        self.name=name

    def __get__(self,instance,owner):
        print(f'__get__ {instance}{owner}')
        return self.name

    def __set__(self,instance,value):
         print(f'__get__ {instance}{value}')
         self.name=value

    def __delete__(self,instance):
        print(f'__delete__{instance}')
        del self.name


class MyObj(object):
    a=Desc('aaaa')
    b=Desc('bbbb')

my_object=MyObj()
print(my_object.a)

my_object.a=456
print(my_object.a)