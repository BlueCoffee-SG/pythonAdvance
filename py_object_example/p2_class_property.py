class Human(object):
    #静态资源
    live=True
    def __init__(self,name) -> None:
        #普通字段
        self.name=name



if __name__=="__main__":

    man=Human("admin")
    woman=Human("Eve")

    #有静态字段，live属性
    Human.__dict__
    #有普通字段，name属性
    man.__dict__

    # 实例可以使用普通字段也可以使用静态字段
    man.name
    man.live=False

    #查看实例属性
    man.__dict__
    man.live
    woman.live
    
    #类可以使用静态字段
    Human.live

    #可以使用类添加静态字段
    Human.newattr=1
    dir(Human)
    Human.__dict__

    #django使用
    #内置类型不能增加属性与方法
    #为一个类 添加一个属性

    setattr(list,'newattr','value')
    #TypeError 不能给内置的类，添加一个属性

    #显示object类所有子类
    print(().__class__.__base__[0].__subclasses__())

