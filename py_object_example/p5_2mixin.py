# <<python gui programing with tkinter>>
# mixin类无法单独使用， 必须和其它类混合傅，来加强基他类

class Displayer():
    def display(self,message):
        print(message)


class LoggerMixin():
    def log(self,message,filename="logfile.txt"):
        with open(filename,'a') as fh:
            fh.write(message)

    def display(self,message):
        super(LoggerMixin,self).display(message)
        self.log(message)

class MySubClass(LoggerMixin,Displayer):
    def log(self, message):
        super().log(message, filename='sublasslog.txt')


subclass=MySubClass()
subclass.display("this string will be shown and logged in subclasslog.txt")
print(MySubClass.mro())