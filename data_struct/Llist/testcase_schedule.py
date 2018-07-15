#_*_ coding: utf-8 _*_
import unittest
from link_list_test import LlistTest

if __name__ == '__main__':
    '''用例的调度组织'''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LlistTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    #将测试结果输出到文件"e:\\UnittestTextReport.txt"
    # with open('e:\\UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)