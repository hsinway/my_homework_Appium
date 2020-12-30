from appium.webdriver.common.mobileby import MobileBy

from ent_Wechat_PO_20201227_Sun.page.base_page import BasePage
from ent_Wechat_PO_20201227_Sun.page.member_info_page import MemberInfoPage
from ent_Wechat_PO_20201227_Sun.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录PO
    """

    def click_add_member(self):
        """
        添加成员
        :return:
        """

        # todo 点击添加成员
        print("address_list_page->点击添加成员")
        # self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return MemberInviteMenuPage(self.driver)

    def click_member(self):
        print("address_list_page->点击成员user9")
        # self.swip_find_click(MobileBy.XPATH, f"//*[@text='{user}']")
        self.swip_find_click(MobileBy.XPATH, "//*[@text='user9']")
        return MemberInfoPage(self.driver)
