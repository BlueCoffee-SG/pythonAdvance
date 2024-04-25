from abc import ABCMeta ,abstractmethod

class Base(metaclass=ABCMeta):   #定义抽象基类
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass


c=Concrete() # typeError