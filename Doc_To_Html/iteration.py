#_*_ coding: utf-8 _*_

#self.description  此demo讲解生成器和迭代器原理

#生成器原理：函数可以产生多个值，每次产生一个值使用yield返回，函数就会被冻结，函数停在那里等待被重新唤醒，
#函数被重新唤醒后就从停止的那点开始执行.
def lines(file):
    for line in file:
        yield line

# if __name__=='__main__':
#     f=open(r'D:\03F_DISK\test.log','r')
#     for temp in lines(f):
#         print temp


#迭代器原理：所谓迭代器就是具有__iter__方法和next方法的对象.
#__iter__方法返回迭代器本身
#next方法返回一个值，当迭代器无值返回时，可以在next方法引发一个StopIteration，迭代时产生异常迭代停止.
class Fibs:

    def __init__(self):
        self.a=1
        self.b=2

    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    def __iter__(self):
        return self

if __name__=='__main__':

    fibs=Fibs()
    for i in fibs:
        print i