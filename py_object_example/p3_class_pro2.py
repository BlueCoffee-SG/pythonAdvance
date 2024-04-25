class Human2(object):
    #人为约定不可以修改,可见属性，但不去修改,内部属性
    _age=0

    #私有属性，不可见
    __fly=False

    #魔术方法(变量的属性随环境变化而变化)，不会自动改名
    # 如 __init__, __name__,  __dict__

#自动改名机制
Human2.__dict__