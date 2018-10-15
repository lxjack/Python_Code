#_*_ coding: utf-8 _*_
import unittest
from Uniform_Autos.link_list import Llist

class TC_delete_list(unittest.TestCase):

    def setUp(self):
        self.logger.info("delete_list setup.")  # 写日志

    def test_delete_list(self):
        '''
        case:测试函数delete_list功能

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

        self.logger.info("delete_list process.")

    def tearDown(self):

        self.logger.info("delete_list teardown.")
