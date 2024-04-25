from typing import Any


class Human2(object):
    '''
    拦截已经有的属性
    '''
    def __init__(self) -> None:
        self.age=10

    def __getattribute__(self, item) -> Any:
        print(f'__getattribute__ called item:{item}')
        return super().__getattribute__(item)
    
h1=Human2()

print(h1.age)
#存在在属性返回取值
print(h1.noattr)
#不存在在属性返回 attributeError

#思考： 为什么使用super()不使用self