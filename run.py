# -*- coding: utf-8 -*-
'a practice of ...'
"入口函数文件"
try:
    from Conf.setting import *  #setting.py
    from util import ReadOpenData, HTMLTestRunner, ClientSelenium
    from util.Base import TimeUtil

except ImportError as error:
    raise error

#入口函数简结
if __name__ == '__main__':
    t_util = TimeUtil() #实例化处理Base TimeUtil
    suite = unittest.defaultTestLoader.discover(TestDir,pattern='test_*.py')  #<TestDir

    fb =open(t_util.get_report_path(), 'wb')
    print("报告的位置：",t_util.get_report_path())
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='本次测试数据', description='结论:')
    runner.run(suite)
    fb.close()