from test_frame.base_page import BasePage
from test_frame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # # self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']").click()
        # self.find_and_click(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        # todo: 因为执行目录是test_search文件,所以要先..到父级目录再找文件
        self.key_value_step_yaml("../page/main.yaml")
        return Market(self.driver)
