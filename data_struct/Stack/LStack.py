#_*_ coding: utf-8 _*_

class StackUnderflow(ValueError):
    pass

class Node():
    '''
    返回单个链表节点
    '''
    def __init__(self,element,next=None):
        self.element=element
        self.next = next

class Link_Stack():
    '''利用链式结构实现数据结构栈'''
    def __init__(self):
        self.head=None

    def is_empty_stack(self):
        return self.head==None

    def length(self):
        '''节点指针个数  即为栈长度  原理：统计节点个数'''
        num = 0
        p = self.head
        while p:
            num = num + 1
            p = p.next
        return num

    def top(self):
        '''查询栈顶元素'''
        if self.is_empty_stack():
            raise StackUnderflow("stack is empty")

        return self.head.element

    def push(self,elem):
        '''元素入栈'''
        temp_node=Node(elem,self.head)
        self.head=temp_node

    def pop(self):
        '''元素出栈'''
        if self.is_empty_stack():
            raise StackUnderflow("stack is empty")

        temp_elem=self.head.element
        self.head=self.head.next

        return temp_elem
