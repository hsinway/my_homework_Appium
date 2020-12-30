from appium.webdriver.common.mobileby import MobileBy

from ent_Wechat_PO_20201227_Sun.page.base_page import BasePage


class ContactAddPage(BasePage):
    """
    成员信息编辑
    """

    def add_contact(self):
        """
        添加信息
        :return:
        """

        # todo 填写姓名,性别,手机号填写
        print("contact_add_page->填写姓名,性别,手机号填写")
        self.find_send_keys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']", "user9")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        self.wait_until_exist(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_send_keys(MobileBy.XPATH,
                            "//*[contains(@text,'手机')]/..//*[@text='手机号']", "13000000009")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return self.get_toast_text()
