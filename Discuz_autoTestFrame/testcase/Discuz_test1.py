# import sys
# sys.path.append('D:/自动化测试/py_workspace/Discuz_autoTestFrame')
from testcase.basetestcase import BaseTestCase
from pageobjects.homepage import HomePage
from pageobjects.base import BasePage
import time
class Search1(BaseTestCase):

    def test_search(self):
        """
        Discuz业务流程一
        :return:
        """
        #声明HomePage对象
        home_page=HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.login("admin","lyf2580")
        time.sleep(3)

        #判断admin是否登录成功
        admin_online_text=base_page.gettext(*home_page.online_admin_loc)
        print("在线用户：",admin_online_text)
        self.assertEqual(admin_online_text,"admin",msg="在线用户不是管理员")

        home_page.moren_click()
        time.sleep(3)
        home_page.fatie("我是发帖内容！！！","我是发帖标题！！！")
        home_page.huitie("我在这边回帖！！！")
        home_page.logout1()

        #通过title判断是否退出成功
        index_page_title=base_page.get_webtitle()
        self.assertEqual(index_page_title,"我是发帖内容！！！ - 默认版块 - Discuz! Board - Powered by Discuz!",msg="当前页面不是Discuz首页")
        self.driver.implicitly_wait(10)




