#_*_ coding: utf-8 _*_
#使用format进行字符串格式化

#使用位置参数，进行字符串格式化
str="my name is {0},i am {1} years old."
name='jane'
age="ten"
temp=str.format(name,age)
print temp

#使用关键字参数，进行字符串格式化
str="Coordinates: {latitude}, {longitude}."
temp=str.format(latitude='37.24N', longitude='-115.81W')
print temp

#使用对象，进行字符串格式化
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

str='Point({obj.x}, {obj.y} ,{z})'
temp_point=Point(4, 2)
temp=str.format(obj=temp_point,z=11)
print temp
