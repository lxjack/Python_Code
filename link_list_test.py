#_*_ coding: utf-8 _*_
import unittest
from link_list import Llist
from link_list import LinkedListOperateError

class LlistTest(unittest.TestCase):

    '''my linked list unittest'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_empty_list(self):
        '''
        case1:测试函数is_empty_list功能 
        
        1、当链表为空时返回True
        2、当链表不为空时返回False
        '''
        temp_list=Llist()
        value=temp_list.is_empty_list()
        self.assertEqual(value,True,"value_info "+str(value))

        temp_list.append(1)
        value = temp_list.is_empty_list()
        self.assertEqual(value,False,"value_info "+str(value))

    def test_delete_list(self):
        '''
        case2:测试函数delete_list功能

        1、删除空链表，链表仍为空
        2、删除非空链表，链表为空
        '''
        temp_list = Llist()
        temp_list.delete_list()
        value = temp_list.is_empty_list()
        self.assertEqual(value, True, "value_info " + str(value))

        temp_list.append(1)
        temp_list.delete_list()
        value = temp_list.is_empty_list()
        self.assertEqual(value, True, "value_info " + str(value))

    def test_prepend(self):
        '''
        case3:测试prepend函数
        
        1、使用prepend添加1个元素'a'，索引0为元素'a'
        2、使用prepend再添加1个元素'b'，索引0为元素'b'；索引1为元素'a'      
        '''
        temp_list = Llist()
        temp_list.prepend('a')
        value=temp_list.index(0)
        self.assertEqual(value, 'a', "value_info " + str(value))

        temp_list.prepend('b')
        value = temp_list.index(0)
        self.assertEqual(value, 'b', "value_info " + str(value))

        value = temp_list.index(1)
        self.assertEqual(value, 'a', "value_info " + str(value))

    def test_append(self):
        '''
        case4:测试append函数

        1、使用append添加1个元素'a'，索引0为元素'a'
        2、使用append再添加1个元素'b'，索引0为元素'a'；索引1为元素'b'
        3、使用append再添加1个元素'c'，索引2为元素'c'        
        '''
        temp_list = Llist()
        temp_list.append('a')
        value = temp_list.index(0)
        self.assertEqual(value, 'a', "value_info " + str(value))

        temp_list.append('b')
        value = temp_list.index(0)
        self.assertEqual(value, 'a', "value_info " + str(value))

        value = temp_list.index(1)
        self.assertEqual(value, 'b', "value_info " + str(value))

        temp_list.append('c')
        value = temp_list.index(2)
        self.assertEqual(value, 'c', "value_info " + str(value))

    def test_middle_pend(self):
        '''
        case5:测试middle_pend函数
        
        1、当被插入元素链表length<2，抛出指定异常
        2、原链表存在2个元素[1，2]，使用middle_pend在索引1添加元素'a'，索引1为元素'a'，索引0为元素1，索引2为元素2
        3、原链表存在3个元素[1，'a'，2] , 使用middle_pend在索引2添加元素'b',索引1为元素'a'，索引2为元素'b'，索引3为元素2
        4、原链表存在4个元素[1，'a','b',2]，指定插入index=0或4，抛出指定异常
        '''
        '''step 1'''
        temp_list = Llist()
        temp_list.append(1)
        with self.assertRaisesRegexp(LinkedListOperateError,'the length of list is less than 2,can not execute middle_pend'):
            temp_list.middle_pend(0,'aaa')

        '''step 2'''
        temp_list.append(2)
        temp_list.middle_pend(1,'a')
        value = temp_list.index(1)
        self.assertEqual(value, 'a', "value_info " + str(value))

        value = temp_list.index(0)
        self.assertEqual(value, 1, "value_info " + str(value))

        value = temp_list.index(2)
        self.assertEqual(value, 2, "value_info " + str(value))

        '''step 3'''
        temp_list.middle_pend(2, 'b')
        value = temp_list.index(1)
        self.assertEqual(value, 'a', "value_info " + str(value))

        value = temp_list.index(2)
        self.assertEqual(value, 'b', "value_info " + str(value))

        value = temp_list.index(3)
        self.assertEqual(value, 2, "value_info " + str(value))

        '''step 4'''
        with self.assertRaisesRegexp(LinkedListOperateError,'the input index can not execute middle_pend'):
            temp_list.middle_pend(0,'aaa')

        with self.assertRaisesRegexp(LinkedListOperateError,'the input index can not execute middle_pend'):
            temp_list.middle_pend(4,'aaa')

    def test_prepop(self):
        '''
        case6:测试prepop函数
        
        1、链表存在2个元素[1，2]，使用prepop函数，删除元素，被删除元素为1
        2、使用prepop函数，再次删除元素，被删除元素为2
        3、使用prepop函数，再次删除元素，抛出指定异常
        '''
        temp_list = Llist()
        temp_list.append(1)
        temp_list.append(2)
        value = temp_list.prepop()
        self.assertEqual(value, 1, "value_info " + str(value))

        value = temp_list.prepop()
        self.assertEqual(value, 2, "value_info " + str(value))

        with self.assertRaisesRegexp(LinkedListOperateError, 'list is empty'):
            temp_list.prepop()

    def test_pop(self):
        '''
        case7:测试pop函数

        1、链表存在2个元素[1，2,'a']，使用pop函数，删除元素，被删除元素为'a'
        2、使用pop函数，再次删除元素，被删除元素为2
        3、使用pop函数，再次删除元素，被删除元素为1
        4、使用pop函数，再次删除元素，抛出指定异常
        '''
        temp_list = Llist()
        temp_list.append(1)
        temp_list.append(2)
        temp_list.append('a')

        value = temp_list.pop()
        self.assertEqual(value,'a', "value_info " + str(value))

        value = temp_list.pop()
        self.assertEqual(value,2, "value_info " + str(value))

        value = temp_list.pop()
        self.assertEqual(value,1, "value_info " + str(value))

        with self.assertRaisesRegexp(LinkedListOperateError, 'list is empty'):
            temp_list.pop()

    def test_middle_pop(self):
        '''
        case8:测试middle_pop函数

        1、当被插入元素链表length=2，抛出指定异常        
        2、原链表存在4个元素[1，2,'a','b'],指定删除index=0或3元素，抛出指定异常        
        3、原链表存在4个元素[1，2,'a','b']，删除index=2元素，删除元素为'a'        
        4、原链表存在3个元素[1,2,'b']，删除index=1元素，删除元素为2
        '''
        '''step 1'''
        temp_list = Llist()
        temp_list.append(1)
        temp_list.append(2)
        with self.assertRaisesRegexp(LinkedListOperateError,'the length of list is less than 3,can not execute middle_pop'):
            temp_list.middle_pop(1)

        '''step 2'''
        temp_list.append('a')
        temp_list.append('b')
        with self.assertRaisesRegexp(LinkedListOperateError, 'the input index can not execute middle_pop'):
            temp_list.middle_pop(0)

        with self.assertRaisesRegexp(LinkedListOperateError, 'the input index can not execute middle_pop'):
            temp_list.middle_pop(3)

        '''step 3'''
        value = temp_list.middle_pop(2)
        self.assertEqual(value, 'a', "value_info " + str(value))

        '''step 4'''
        value = temp_list.middle_pop(1)
        self.assertEqual(value, 2, "value_info " + str(value))

    def test_find_node(self):
        '''
        case9:测试find_node函数

        1、当链表为空时，调用find_node函数，抛出指定异常        
        2、原链表存在4个元素[1，2,'a','b'],指定索引index=-1或4元素，抛出指定异常                
        3、原链表存在4个元素[1，2,'a','b']，指定索引index=0，找到节点0
        4、原链表存在4个元素[1，2,'a','b']，指定索引index=3，找到节点3        
        '''
        '''step 1'''
        temp_list = Llist()
        with self.assertRaisesRegexp(LinkedListOperateError,'list is empty'):
            temp_list.find_node(1)

        '''step 2'''
        temp_list.append(1)
        temp_list.append(2)
        temp_list.append('a')
        temp_list.append('b')
        with self.assertRaisesRegexp(LinkedListOperateError, 'list index out of range'):
            temp_list.find_node(-1)

        with self.assertRaisesRegexp(LinkedListOperateError, 'list index out of range'):
            temp_list.find_node(4)

        '''step 3'''
        p=temp_list.find_node(0)
        value = p.element
        self.assertEqual(value, 1, "value_info " + str(value))

        '''step 4'''
        p = temp_list.find_node(3)
        value = p.element
        self.assertEqual(value, 'b', "value_info " + str(value))

    def test_index(self):
        '''
        case10:测试index函数

        1、当链表为空时，调用index函数，抛出指定异常        
        2、原链表存在4个元素[1，2,'a','b'],指定索引index=-1或4元素，抛出指定异常                
        3、原链表存在4个元素[1，2,'a','b']，指定索引index=0，找到节点0
        4、原链表存在4个元素[1，2,'a','b']，指定索引index=3，找到节点3        
        '''
        '''step 1'''
        temp_list = Llist()
        with self.assertRaisesRegexp(LinkedListOperateError, 'list is empty'):
            temp_list.index(1)

        '''step 2'''
        temp_list.append(1)
        temp_list.append(2)
        temp_list.append('a')
        temp_list.append('b')
        with self.assertRaisesRegexp(LinkedListOperateError, 'list index out of range'):
            temp_list.index(-1)

        with self.assertRaisesRegexp(LinkedListOperateError, 'list index out of range'):
            temp_list.index(4)

        '''step 3'''
        value = temp_list.index(0)
        self.assertEqual(value, 1, "value_info " + str(value))

        '''step 4'''
        value = temp_list.index(3)
        self.assertEqual(value, 'b', "value_info " + str(value))

    def test_modify_element(self):
        '''
        case11:测试modify_element函数

        1、当链表为空时，调用modify_element函数，抛出指定异常        
        2、原链表存在4个元素[1，2,'a','b'],指定索引index=-1或4元素，抛出指定异常
                        
        3、原链表存在4个元素[1，2,'a','b']，修改索引index=0元素为'aa'
        4、原链表存在4个元素[1，2,'a','b']，修改索引index=3元素为'cc'     
        '''
        '''step 1'''
        temp_list = Llist()
        with self.assertRaisesRegexp(LinkedListOperateError, 'list is empty'):
            temp_list.modify_element(1,'aa')

        '''step 2'''
        temp_list.append(1)
        temp_list.append(2)
        temp_list.append('a')
        temp_list.append('b')
        with self.assertRaisesRegexp(LinkedListOperateError, 'list index out of range'):
            temp_list.modify_element(-1,'aa')

        with self.assertRaisesRegexp(LinkedListOperateError, 'list index out of range'):
            temp_list.modify_element(4,'aa')

        '''step 3'''
        temp_list.modify_element(0, 'aa')
        value = temp_list.index(0)
        self.assertEqual(value, 'aa', "value_info " + str(value))

        '''step 4'''
        temp_list.modify_element(3, 'cc')
        value = temp_list.index(3)
        self.assertEqual(value, 'cc', "value_info " + str(value))

    def test_length(self):
        '''
        case12:测试length函数

        1、当链表为空时，调用length函数，返回链表长度为0        
        2、原链表存在4个元素[1，2,'a','b'],调用length函数，返回链表长度为4    
        '''
        '''step 1'''
        temp_list = Llist()
        value = temp_list.length()
        self.assertEqual(value, 0, "value_info " + str(value))

        '''step 2'''
        temp_list.append(1)
        temp_list.append(2)
        temp_list.append('a')
        temp_list.append('b')
        value = temp_list.length()
        self.assertEqual(value, 4, "value_info " + str(value))

if __name__=="__main__":

    unittest.main()