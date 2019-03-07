import sys
sys.path.append('D:/自动化测试/py_workspace/Discuz_autoTestFrame')

from testcase.Discuz_test1 import Search1
from testcase.Discuz_test2 import Search2
from testcase.Discuz_test3 import Search3
from testcase.Discuz_test4 import Search4
import unittest
import HTMLTestRunner
import os
import time

# 设置报告文件保存路径
repoter_path = os.path.dirname(os.path.abspath('.'))+ '/repoter/'
# print("+++++++++++++++++",repoter_path)
# if not os.path.exists(repoter_path):
# #     os.mkdir(repoter_path)
now=time.strftime(('%Y-%m-%d-%H_%M_%S'),time.localtime(time.time()))
html_repoter = repoter_path +now+"_result.html"
fp = open(html_repoter, "wb")

# 构造测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Search1))
suite.addTest(unittest.makeSuite(Search2))
suite.addTest(unittest.makeSuite(Search3))
suite.addTest(unittest.makeSuite(Search4))
if __name__ == "__main__":
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)
