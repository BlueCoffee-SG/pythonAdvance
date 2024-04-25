class Human(object):
    def __init__(self) :
        self.name=None
        self.gender=None

    def getName(self):
        return self.name
    
    def getGender(self):
        return self.gender
    

class Man(Human):
    def __init__(self,name):
        print(f'Hi,man {name}')



class Woman(Human):
    def __init__(self,name):
        print(f'Hi,woman {name}')

class Factory:
    def getPerson(self,name,gender):
        if gender=='M':
            return Man(name)
        
        elif gender=='F':
            return Woman(name)
        

if __name__=='__main__':
    factory=Factory()
    person=factory.getPerson("adam",'M')




#返回在函数内动态创建的类
def factory2(func):
    class Klass:pass 
    #setattr 需要三个参数：对象，key, value
    print(func)
    setattr(Klass,func.__name__,func)
    return Klass


def say_foo(say_foo):
    print('bar')


Foo=factory2(say_foo)
foo=Foo()
foo.say_foo()