#_*_ coding: utf-8 _*_

class StackUnderflow(ValueError):
    pass

class Seq_Stack():

    def __init__(self):
        self._elems=[]

    def is_empty_stack(self):
        return self._elems==[]

    def length(self):
        return len(self._elems)

    def top(self):

        if self.is_empty_stack():
            raise StackUnderflow("stack is empty")

        return self._elems[-1]

    def push(self,elem):
        self._elems.append(elem)

    def pop(self):

        if self.is_empty_stack():
            raise StackUnderflow("stack is empty")

        return self._elems.pop()

