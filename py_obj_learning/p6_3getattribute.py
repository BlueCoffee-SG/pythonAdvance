
class Human2(object):

    def __getattribute__(self, item) -> Any:
        '''
        将不存在的属性设置为100并返回, 模拟getattr行为
        '''
        print('Human2:__getattribute__')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item]=100  # item 实例有什么样的属性，就会被注册到__dict__
            return 100
    
h1=Human2()

print(h1.noattr)

#思考 有更简洁的写法吗？