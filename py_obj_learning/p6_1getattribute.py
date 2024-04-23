from typing import Any


class Human(object):
    # 接受参数
    def __init__(self,name):
        self.name=name


h1=Human("adam")
h2=Human("Eve")

#对例属性做占位性
h1.name='python'

#对实例属性查询
h1.name

#删除实例属性
del h1.name


#AttirbuteError 访问不存在在属性
#由__getattribute__(self,name)抛出
h1.name


##############
class Human2(object):
    '''
    getattribute对任意读取的属性进行截获

    '''
    def __init__(self) -> None:
        self.age=10

    def __getattribute__(self, item) -> Any:
        print(f'__getattirbute__ called item:{item}')


h1=Human2()
h1.age
h1.noattr