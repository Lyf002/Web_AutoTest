from testcase.basetestcase import BaseTestCase
from pageobjects.homepage import HomePage
from pageobjects.base import BasePage
import time
class Search4(BaseTestCase):

    def test_search4(self):
        """
        Discuz业务流程四
        :return:
        """
        home_page = HomePage(self.driver)
        base_page=BasePage(self.driver)
        home_page.login("admin", "lyf2580")
        home_page.moren_click()
        #判断是否进入默认板块
        moren_part_text=base_page.gettext(*home_page.moren_text_loc)
        self.assertEqual(moren_part_text,"默认版块",msg="进入默认板块失败")
        home_page.vote_fatie("投票标题","001","002","003","投票文本内容")

