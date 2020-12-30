from appium.webdriver.common.mobileby import MobileBy

from ent_Wechat_PO_20201227_Sun.page.base_page import BasePage


class MemberInfoPage(BasePage):
    def delete_member(self):
        print("member_info_page->删除成员")
        self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ie0']")
        self.find_and_click(MobileBy.XPATH,"//*[@text='编辑成员']")
        self.find_and_click(MobileBy.XPATH,"//*[@text='删除成员']")
        self.wait_until_exist(MobileBy.XPATH, "//*[contains(@text,'完全清除')]")
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        self.wait_until_exist(MobileBy.XPATH, "//*[contains(@text,'企业通讯录')]")
        self.wait_until_not_exist(MobileBy.XPATH, "//*[@text='user9']")
        return self.driver.page_source

