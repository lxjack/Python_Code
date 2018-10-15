# _*_ coding: utf-8 _*_
import unittest
from Uniform_Autos.link_list import Llist
from Uniform_Autos.link_list import LinkedListOperateError

class TC_index_insert(unittest.TestCase):

    def setUp(self):
        self.logger.info("index_insert setup.")  # 写日志

    def test_index_insert(self):
        '''
        case:测试index_insert函数

        1、当链表为空时，在索引0插入元素'a'，索引index=0元素为'a'
        2、当链表为['a']时，在索引1插入元素'b'，索引index=1元素为'b'
        3、当链表为['a','b']时，在索引1插入元素'c'，索引index=1元素为'c',索引index=2元素为'b'
        4、当链表为['a','c','b']时，传入索引>=4或<=-1或非数字，抛出指定异常
        '''
        '''step 1'''
        temp_list = Llist()
        temp_list.index_insert(0,'a')
        value =temp_list.index(0)
        self.assertEqual(value, 'a', "value_info " + str(value))

        '''step 2'''
        temp_list.index_insert(1, 'b')
        value = temp_list.index(1)
        self.assertEqual(value, 'b', "value_info " + str(value))

        '''step 3'''
        temp_list.index_insert(1, 'c')
        value = temp_list.index(1)
        self.assertEqual(value, 'c', "value_info " + str(value))

        value = temp_list.index(2)
        self.assertEqual(value, 'b', "value_info " + str(value))

        '''step 4'''
        with self.assertRaisesRegexp(LinkedListOperateError, 'index is out of range or index not a integer'):
            temp_list.index_insert(4, 'ccc')
        with self.assertRaisesRegexp(LinkedListOperateError, 'index is out of range or index not a integer'):
            temp_list.index_insert(-1, 'ccc')
        with self.assertRaisesRegexp(LinkedListOperateError, 'index is out of range or index not a integer'):
            temp_list.index_insert('aaa', 'ccc')

        self.logger.info("index_insert process.")


    def tearDown(self):
        self.logger.info("index_insert teardown.")
