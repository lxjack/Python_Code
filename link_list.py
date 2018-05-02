#_*_ coding: utf-8 _*_

class Node():
    '''
    返回链表单个节点
    '''
    def __init__(self,element,next=None):
        self.element=element
        self.next = next

class Llist():

    def __init__(self):
        '''初始化空链表'''
        self.head=None

    def create_empty_list(self):
        '''1.将链表置为空表'''
        self.head = None

    def is_empty_list(self):
        '''2.判断链表是否为空链表'''
        if self.head==None:
            return True
        else:
            return False

    def length(self):
        '''3.计算表长度'''
        num=0
        p=self.head
        while p:
            num=num+1
            p=p.next
        return num

    def append(self,element):
        '''4.表尾端加入元素'''

        '''当表为空表时'''
        if self.head==None:
            pt=Node(element)
            self.head=pt
            return 1
        '''当表不为空表时'''
        if self.head != None:
            '''寻找表尾节点'''
            p=self.head
            while True:
                if p.next==None:
                    break
                else:
                    p=p.next
            '''创建节点 原表尾链接链接到新生成节点'''
            pt = Node(element)
            p.next=pt
            return 1

    def prepend(self,element):
        '''5.表尾端加入元素'''
        pt = Node(element)
        pt.next=self.head
        self.head=pt

    def index(self,i):
        '''6.按下标进行元素索引'''

        if self.head==None:
            print "link list is empty."
            return 1
        elif i<0 or i>=self.length():
            print "index is out of range."
            return 1
        else:
            p=self.head
            n=0
            while p:
                if n==i:
                    break
                else:
                    p=p.next
                    n=n+1
            return p.element

    def prepop(self):
        '''7.删除表首元素'''
        if self.head==None:
            print "link list is empty."
            return 1
        else:
            et=self.head.element
            self.head=self.head.next
            return et

    def pop(self):
        '''8.删除表尾元素'''
        if self.head==None:
            print "link list is empty."
            return 1
        elif self.length()==1:
            et=self.head.element
            self.head=None
            return et
        else:
            p=self.head
            while p:
                if p.next.next==None:
                    '''找到删除节点的前一个节点指针'''
                    break
                else:
                    p=p.next
            et=p.next.element
            p.next=None
            return et

    def print_all_list(self):
        '''9.打印表中所有元素'''
        p=self.head
        if p==None:
            print "empty list"
            return 1
        print ">>>list info begin:"
        while p:
            print p.element
            p=p.next
        print ">>>list info end."



l1=Llist()
l1.append('a')
l1.append('b')
l1.append('c')
l1.append('d')

print l1.pop()
l1.print_all_list()

print l1.pop()
l1.print_all_list()

print l1.pop()
l1.print_all_list()

print l1.pop()
l1.print_all_list()

print l1.pop()
l1.print_all_list()