from appium.webdriver.common.mobileby import MobileBy

from ent_Wechat_PO_20201227_Sun.page.base_page import BasePage
from ent_Wechat_PO_20201227_Sun.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    """
    添加成员PO
    """

    def add_member_manual(self):
        """
        手动添加成员信息
        :return:
        """
        # todo 点击手动添加成员信息
        print("member_invite_menu_page->点击手动添加成员信息")
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAddPage(self.driver)
