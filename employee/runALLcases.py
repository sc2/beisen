
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

if __name__ == "__main__":
    # 定义一个测试用例的存放地址
    test_dir = "./TestCases/"
    # 把测试报告加入discover容器
    discover = unittest.defaultTestLoader.discover(test_dir, "*.py")

    # 定义一个测试报告的存放地址
    testReportDir = "./reports/"
    # 定义测试报告的名字
    nowTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    fileName = nowTime + ".html"
    # 定义路径和测试报告的名字
    testReportDir_FileName = testReportDir + fileName

    # 打开测试报告文件，并赋予可读写权限
    fp = open(testReportDir_FileName, 'wb')

    # 把测试结果内容写到测试报告里面,并装载到HTMLTestRunner模块
    runner = HTMLTestRunner(stream=fp, title="自动化测试报告", description="用例执行情况")

    # 运行测试用例
    runner.run(discover)

    # 关闭文件
    fp.close()
