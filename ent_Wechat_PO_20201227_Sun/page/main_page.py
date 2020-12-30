from appium.webdriver.common.mobileby import MobileBy

from ent_Wechat_PO_20201227_Sun.page.address_list_page import AddressListPage
from ent_Wechat_PO_20201227_Sun.page.base_page import BasePage


class MainPage(BasePage):
    """
    首页PO
    """

    # 直接封装在父类中
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        # todo 点击通讯录按钮
        print("\nmain_page->点击通讯录按钮")
        self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")
        return AddressListPage(self.driver)
