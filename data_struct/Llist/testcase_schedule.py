#_*_ coding: utf-8 _*_
import unittest
from link_list_test import LlistTest
import HTMLTestRunner
import time

if __name__ == '__main__':
    '''用例的调度组织'''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LlistTest))

    #获取时间  定义测试报告名字
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    report_name="./"+now+"my_report.html"

    fp = file(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )

    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
    runner.run(suite)