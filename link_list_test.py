#_*_ coding: utf-8 _*_
import unittest
from link_list import Llist

class LlistTest(unittest.TestCase):

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


if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest("test_is_empty_list")
    suite.addTest("test_delete_list")
    suite.addTest("test_prepend")

    runner=unittest.TextTestRunner()
    runner.run(suite)