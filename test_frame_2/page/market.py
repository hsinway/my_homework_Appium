from test_frame_2.page.search import Search
from test_frame_2.page.pre_page import PrePage


class Market(PrePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.basepage.key_value_step_yaml("../file/market.yaml")
        return Search(self.basepage)
