#_*_ coding: utf-8 _*_

class LinkedListOperateError(ValueError):
    '''自定义链表操作异常类'''
    pass

class Node():
    '''
    返回单个链表节点
    '''
    def __init__(self,element,next=None):
        self.element=element
        self.next = next

class Llist():

    def __init__(self):
        '''1.初始化空链表'''
        self.head=None

    def delete_list(self):
        '''2.删除链表'''
        self.head = None

    def is_empty_list(self):
        '''3.判断链表是否为空链表'''
        if self.head==None:
            return True
        else:
            return False

    def prepend(self,element):
        '''4.1.表首端加入元素'''
        pt = Node(element)
        pt.next=self.head
        self.head=pt

    def append(self,element):
        '''4.2.表尾端加入元素'''

        '''当表为空表时'''
        if self.head==None:
            pt=Node(element)
            self.head=pt
            return

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
            return

    def middle_pend(self,index,element):
        '''4.3.根据索引在链表中间添加元素'''
        if self.length() < 2:
            raise LinkedListOperateError("the length of list is less than 2,can not execute middle_pend")
        if index <=0 or index>=self.length():
            raise LinkedListOperateError("the input index can not execute middle_pend")
        '''找到插入节点的前一节点，进行插入'''
        p=self.find_node(index-1)
        pt = Node(element)
        pt.next=p.next
        p.next=pt

    def prepop(self):
        '''5.1.删除表首元素'''
        if self.head==None:
            raise LinkedListOperateError("list is empty")
        else:
            et=self.head.element
            self.head=self.head.next
            return et

    def pop(self):
        '''5.2.删除表尾元素'''
        if self.head==None:
            raise LinkedListOperateError("list is empty")

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

    def middle_pop(self,index):
        '''5.3.根据索引删除元素'''
        if self.length() <3:
            raise LinkedListOperateError("the length of list is less than 3,can not execute middle_pop")
        if index <=0 or index>=self.length()-1:
            raise LinkedListOperateError("the input index can not execute middle_pop")

        '''找到删除节点的前一节点'''
        p = self.find_node(index - 1)
        et = p.next.element
        p.next = p.next.next
        return et

    def find_node(self,index):
        '''6.根据索引返回节点指针'''
        if self.head==None:
            raise LinkedListOperateError("list is empty")

        if index<0 or index>=self.length():
            raise LinkedListOperateError("list index out of range")

        p=self.head
        n=0
        while True:
            if n==index:
                break
            else:
                p=p.next
                n=n+1
        return p

    def index(self,i):
        '''7.按下标进行元素索引'''
        if self.head==None:
            raise LinkedListOperateError("list is empty")

        if i < 0 or i >= self.length():
            raise LinkedListOperateError("list index out of range")

        p=self.find_node(i)
        return p.element

    def modify_element(self,i,element):
        '''8.根据索引修改节点元素'''
        if self.head == None:
            raise LinkedListOperateError("list is empty")

        if i < 0 or i >= self.length():
            raise LinkedListOperateError("list index out of range")

        p = self.find_node(i)
        p.element=element


    def length(self):
        '''9.计算表长度'''
        num=0
        p=self.head
        while p:
            num=num+1
            p=p.next
        return num

    def print_all_list(self):
        '''10.输出链表'''
        p=self.head
        if p==None:
            print "[]"
        else:
            listinfo ="["
            while p:
                listinfo= listinfo + str(p.element) +","
                p=p.next

            listinfo=listinfo[:-1] + "]"
            print listinfo

    def index_insert(self,i,element):
        '''11.根据索引，向链表中插入元素'''
        if i==0:
            self.prepend(element)
            return
        elif i==self.length():
            self.append(element)
            return
        elif i>=1 and i<=self.length()-1:
            self.middle_pend(i,element)
            return

        raise LinkedListOperateError("index is out of range or index not a integer")

    def index_pop(self,i):
        '''13.根据索引，删除链表元素'''
        if self.head==None:
            raise LinkedListOperateError("list is empty")

        if i<0 or i>=self.length():
            raise LinkedListOperateError("index is out of range")

        if i == 0:
            et=self.prepop()
            return et

        elif i == self.length()-1:
            et=self.pop()
            return et

        elif i >= 1 and i <= self.length() - 2:
            et=self.middle_pop(i)
            return et


if __name__=="__main__":
    '''demo'''
    l1=Llist()
    l1.append(1)
    l1.append(2)

    l1.print_all_list()