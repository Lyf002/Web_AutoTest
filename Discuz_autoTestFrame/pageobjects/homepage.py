from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.logger import Logger
import time
import random

logger=Logger(logger="HomePage").getlog()
class HomePage(BasePage):
    #定位元素
    input_username_loc=(By.ID,"ls_username")
    input_password_loc=(By.ID,"ls_password")
    button_login_loc=(By.CSS_SELECTOR,".fastlg_l em")
    img_link_loc=(By.CSS_SELECTOR,".hdc h2 a img")
    moren_link_loc=(By.CSS_SELECTOR,".bm_c h2 a")
    input_content_loc = (By.CSS_SELECTOR, ".bm_c .pbt input")
    input_title_loc = (By.ID, "fastpostmessage")
    button_submit_loc=(By.ID,"fastpostsubmit")
    button_logout_loc=(By.LINK_TEXT,"退出")
    input_huitie_loc = (By.ID, "fastpostmessage")
    check_box_loc=(By.NAME,"moderate[]")
    button_del_loc = (By.LINK_TEXT, "删除")
    button_sure_loc=(By.ID,"modsubmit")
    manage_center_loc=(By.LINK_TEXT,"管理中心")
    manage_login_pwd_loc = (By.NAME, "admin_password")
    button_manage_login_loc = (By.NAME, "submit")
    luntan_link_loc=(By.ID,"header_forum")
    add_newBankuai_loc=(By.CSS_SELECTOR,".lastboard .addtr")
    input_bkname_loc=(By.NAME,"newforum[1][]")
    submit_editsubmit_loc=(By.ID,"submit_editsubmit")
    mamager_logout_loc=(By.CSS_SELECTOR,".uinfo p a")
    new_part_link_loc=(By.CSS_SELECTOR,".fl_tb tbody tr:nth-last-child(2) td:nth-last-child(3) h2 a")

    input_search_loc=(By.ID,"scbar_txt")
    button_search_loc=(By.CSS_SELECTOR,".scbar_btn_td .pn")
    title_link_loc=(By.CSS_SELECTOR,".xs3 a strong font")
    title_loc=(By.ID,"thread_subject")
    button_fatie_loc=(By.ID,"newspecial")
    start_vote_loc=(By.CSS_SELECTOR,".mbw li:nth-last-child(1) a")
    title_vote_loc=(By.ID,"subject")
    option1_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")
    option2_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    option3_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")
    vote_content_loc=(By.CSS_SELECTOR,"body")
    button_send_vote_loc=(By.ID,"postsubmit")
    radio_option1=(By.CSS_SELECTOR,".pcht tbody tr:nth-child(1)  .pslt input")
    radio_option2 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3)  .pslt input")
    radio_option3 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5)  .pslt input")
    radio_list=[radio_option1,radio_option2,radio_option3]
    submit_vote_loc=(By.CSS_SELECTOR,".pn span")
    radio_title1_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(1) .pvt label")
    radio_title2_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3) .pvt label")
    radio_title3_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5) .pvt label")
    vote1_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(2) td:nth-last-child(1)")
    vote2_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(4) td:nth-last-child(1)")
    vote3_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(6) td:nth-last-child(1)")
    vote_title_loc=(By.CSS_SELECTOR,".vwthd .ts span")

    #断言-----页面元素
    online_admin_loc=(By.CSS_SELECTOR,".vwmy a")
    moren_text_loc=(By.CSS_SELECTOR,".xs2 a")

    # print(type(title_link_loc))

    def login(self,uname,upwd):
        self.sendkeys(uname,*self.input_username_loc)
        self.sendkeys(upwd, *self.input_password_loc)
        self.click(*self.button_login_loc)
        time.sleep(5)
        webtitle=self.get_webtitle()
        return webtitle

    def moren_click(self):
        self.click(*self.moren_link_loc)
        time.sleep(2)

    def fatie(self,content,title):
        self.sendkeys(content, *self.input_content_loc)
        self.sendkeys(title, *self.input_title_loc)
        self.click(*self.button_submit_loc)

    def logout1(self):
        self.click(*self.button_logout_loc)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.current_window_handle)
        time.sleep(3)

    def del_tie(self):
        self.click(*self.check_box_loc)
        self.click(*self.button_del_loc)
        self.click(*self.button_sure_loc)

    def huitie(self,content):
        self.sendkeys(content, *self.input_huitie_loc)

    def manage_center(self,password):
        self.click(*self.manage_center_loc)
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])

        try:
            # assert "登录管理中心" in self.driver.title
            #激活新窗口
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.info("Switch to current window successfully")
            self.sendkeys(password, *self.manage_login_pwd_loc)
            self.click(*self.button_manage_login_loc)
            self.driver.implicitly_wait(10)
            webtitle = self.get_webtitle()
            return webtitle
        except Exception as e:
            logger.error("Failed to switch to current window.")
        self.click(*self.luntan_link_loc)
        self.driver.implicitly_wait(10)

    def add_new_part(self,bk_name):
        #激活iframe
        self.driver.switch_to.frame(0)
        self.click(*self.add_newBankuai_loc)
        self.clear(*self.input_bkname_loc)
        self.sendkeys(bk_name,*self.input_bkname_loc)
        self.click(*self.submit_editsubmit_loc)

    def click_new_part(self):
        self.click(*self.new_part_link_loc)
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def logout2(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.mamager_logout_loc)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(10)

    def search(self,content):
        self.clear(*self.input_search_loc)
        self.sendkeys(content,*self.input_search_loc)
        self.click(*self.button_search_loc)
        self.driver.implicitly_wait(20)
        self.driver.switch_to.window(self.driver.window_handles[1])
        webtitle = self.get_webtitle()
        return webtitle
    def title_click(self):
        self.click(*self.title_link_loc)
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[2])
        webtitle = self.get_webtitle()
        return webtitle

    def vote_fatie(self,title,option1,option2,option3,vote_content):
        self.click(*self.button_fatie_loc)
        self.click(*self.start_vote_loc)
        self.sendkeys(title,*self.title_vote_loc)
        self.sendkeys(option1,*self.option1_vote_loc)
        self.sendkeys(option2,*self.option2_vote_loc)
        self.sendkeys(option3,*self.option3_vote_loc)
        self.driver.switch_to.frame(0)
        self.sendkeys(vote_content,*self.vote_content_loc)
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.click(*self.button_send_vote_loc)
        self.vote()
        logger.info("选项名称及投票比例：")
        title1=self.gettext(*self.radio_title1_loc)
        percent1 = self.gettext(*self.vote1_percent_loc)
        logger.info("投票选项1标题：%s"%title1)
        logger.info("投票选项1比例：%s"%percent1)
        title2 = self.gettext(*self.radio_title2_loc)
        percent2 = self.gettext(*self.vote2_percent_loc)
        logger.info("投票选项2标题：%s"%title2)
        logger.info("投票选项2比例：%s"%percent2)
        title3 = self.gettext(*self.radio_title3_loc)
        percent3 = self.gettext(*self.vote3_percent_loc)
        logger.info("投票选项3标题：%s"%title3)
        logger.info("投票选项3比例：%s"%percent3)
        mainTitle=self.gettext(*self.vote_title_loc)
        logger.info("投票标题：%s"%mainTitle)

    def vote(self):
        radiosLen=len(list(self.radio_list))
        i=random.randint(0,radiosLen-1)
        print("随机数是：",i)
        self.click(*self.radio_list[i])
        self.click(*self.submit_vote_loc)
        time.sleep(3)







