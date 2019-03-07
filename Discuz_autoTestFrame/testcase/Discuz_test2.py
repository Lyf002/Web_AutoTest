from testcase.basetestcase import BaseTestCase
from pageobjects.homepage import HomePage
from pageobjects.base import BasePage
import time
class Search2(BaseTestCase):

    def test_search2(self):
        """
        业务流程二
        :return:
        """
        #声明HomePage对象
        home_page=HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.login("admin","lyf2580")
        homePage_webtitle=base_page.get_webtitle()
        #判断打开论坛首页是否正确
        self.assertEqual(homePage_webtitle,"【新提醒】论坛 - Powered by Discuz!",msg="%s页面跳转失败"%homePage_webtitle)

        home_page.moren_click()
        home_page.del_tie()
        #弹出登录窗口
        home_page.manage_center("lyf2580")
        managepage_title=base_page.get_webtitle()
        # 判断进入管理中心页面是否正确
        self.assertEqual(managepage_title, "Discuz! Board 管理中心 - 首页", msg="%s页面跳转失败" % managepage_title)

        home_page.add_new_part("新版块01")
        home_page.logout2()
        home_page.logout1()
        home_page.login("嗯哼哈呼嘿", "123456")
        home_page.click_new_part()
        home_page.fatie("我是发帖内容！！！", "我是发帖标题！！！")
        home_page.huitie("我在这边回帖！！！")