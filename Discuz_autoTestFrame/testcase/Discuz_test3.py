from testcase.basetestcase import BaseTestCase
from pageobjects.homepage import HomePage
from pageobjects.base import BasePage
import time
class Search3(BaseTestCase):

    def test_search3(self):
        """
        Discuz业务流程三
        :return:
        """
        home_page = HomePage(self.driver)
        base_page=BasePage(self.driver)

        home_page.login("admin", "lyf2580")
        # 判断打开论坛首页是否正确
        homePage_webtitle=base_page.get_webtitle()
        self.assertEqual(homePage_webtitle, "【新提醒】论坛 - Powered by Discuz!", msg="%s页面跳转失败" % homePage_webtitle)

        #判断点击搜索按钮页面跳转是否正确
        home_page.search("haotest")
        search_page_title=base_page.get_webtitle()
        self.assertEqual(search_page_title, "搜索 - Discuz! Board - Powered by Discuz!", msg="%s页面跳转失败" % homePage_webtitle)

        title_click_page_title=home_page.title_click()
        self.assertEqual(title_click_page_title, "haotest - 默认版块 - Discuz! Board - Powered by Discuz!", msg="%s页面跳转失败" % homePage_webtitle)

        result = base_page.gettext(*home_page.title_loc)
        time.sleep(12)
        self.assertEqual(result, "haotest", msg=result)
        self.driver.switch_to.window(self.driver.window_handles[2])
        home_page.logout1()
