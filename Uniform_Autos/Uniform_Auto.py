#_*_ coding: utf-8 _*_
import unittest
import HTMLTestRunner
import time

if __name__ == '__main__':

    '''通过这段代码   可以进行执行用例的配置化管理（从配置文件中进行读取）'''
    #可根据配置文件动态载入测试用例  方便批量用例的执行
    testcases = [["Uniform_Autos.TEST_CASE.TC_delete_list", "TC_delete_list"],
                 ["Uniform_Autos.TEST_CASE.TC_index_insert", "TC_index_insert"]
                 ]
    suite = unittest.TestSuite()
    for testcase in testcases:
        exec("from %s import %s" % (testcase[0],testcase[1]))
        exec ('''suite.addTests(unittest.TestLoader().loadTestsFromTestCase(%s))''' % testcase[1])

    #获取时间  定义测试报告名字
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    report_name="./"+now+"my_report.html"

    fp = file(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )

    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/6">'
    runner.run(suite)