#_*_ coding: utf-8 _*_

class StackUnderflow(ValueError):
    pass

class Seq_Stack():
    '''利用列表的append和pop特性实现数据结构栈'''
    def __init__(self):
        self._elems=[]

    def is_empty_stack(self):
        return self._elems==[]

    def length(self):
        return len(self._elems)

    def top(self):
        '''查询栈顶元素'''
        if self.is_empty_stack():
            raise StackUnderflow("stack is empty")

        return self._elems[-1]

    def push(self,elem):
        '''元素入栈'''
        self._elems.append(elem)

    def pop(self):
        '''元素出栈'''
        if self.is_empty_stack():
            raise StackUnderflow("stack is empty")

        return self._elems.pop()
