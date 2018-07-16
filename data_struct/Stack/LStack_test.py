#_*_ coding: utf-8 _*_
import unittest
from LStack import Link_Stack
from LStack import StackUnderflow

class Link_StackTest(unittest.TestCase):
    '''my link stack unittest'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_empty_stack(self):
        '''
           case1:测试函数is_empty_stack功能

           1、当栈为空时返回True
           2、当栈表不为空时返回False
        '''
        '''step1'''
        temp_stack = Link_Stack()
        value = temp_stack.is_empty_stack()
        self.assertEqual(value, True, "value_info " + str(value))

        '''step2'''
        temp_stack.push(1)
        value = temp_stack.is_empty_stack()
        self.assertEqual(value, False, "value_info " + str(value))

    def test_length(self):
        '''
        case2:测试length函数
        1、当栈为空时，调用length函数，返回栈长度为0
        2、栈存在2个元素[1，2],调用length函数，返回栈长度为2
        '''
        '''step 1'''
        temp_stack = Link_Stack()
        value = temp_stack.length()
        self.assertEqual(value, 0, "value_info " + str(value))

        '''step 2'''
        temp_stack.push(1)
        temp_stack.push(2)
        temp_stack.push(3)
        temp_stack.pop()
        value = temp_stack.length()
        self.assertEqual(value, 2, "value_info " + str(value))

    def test_top(self):
        '''
        case3:测试top函数
        1、当栈为空时，调用top函数，抛出对应异常
        2、栈存在2个元素[1，2],调用top函数，返回元素值为2，并且栈长度为2
        '''
        '''step 1'''
        temp_stack = Link_Stack()
        with self.assertRaisesRegexp(StackUnderflow, 'stack is empty'):
            temp_stack.top()

        '''step 2'''
        temp_stack.push(1)
        temp_stack.push(2)
        value = temp_stack.top()
        self.assertEqual(value, 2, "value_info " + str(value))
        value = temp_stack.length()
        self.assertEqual(value, 2, "value_info " + str(value))

    def test_push(self):
        '''
        case4:测试push函数
        1、往空栈中添加元素'a'，查询栈顶元素为'a'
        2、往栈中再添加素'b',查询栈顶元素为'b'，并且栈长度为2
        '''
        '''step 1'''
        temp_stack = Link_Stack()
        temp_stack.push('a')
        value = temp_stack.top()
        self.assertEqual(value, 'a', "value_info " + str(value))

        '''step 2'''
        temp_stack.push('b')
        value = temp_stack.top()
        self.assertEqual(value, 'b', "value_info " + str(value))
        value = temp_stack.length()
        self.assertEqual(value, 2, "value_info " + str(value))


    def test_pop(self):
        '''
        case5:测试pop函数
        1、当栈为空时，调用pop函数，抛出异常
        2、栈为['a','b'],弹出栈顶元素，弹出栈顶元素为'b'，栈长度为1
        3、栈为['a'],弹出栈顶元素，弹出栈顶元素为'a'，栈长度为0
        '''
        '''step 1'''
        temp_stack = Link_Stack()
        with self.assertRaisesRegexp(StackUnderflow, 'stack is empty'):
            temp_stack.pop()

        '''step 2'''
        temp_stack.push('a')
        temp_stack.push('b')
        value = temp_stack.pop()
        self.assertEqual(value, 'b', "value_info " + str(value))
        value = temp_stack.length()
        self.assertEqual(value, 1, "value_info " + str(value))

        '''step 3'''
        value = temp_stack.pop()
        self.assertEqual(value, 'a', "value_info " + str(value))
        value = temp_stack.length()
        self.assertEqual(value, 0, "value_info " + str(value))


if __name__=="__main__":

    unittest.main()
