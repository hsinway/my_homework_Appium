from test_frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxx")
        self.key_value_step_yaml("../page/search.yaml")

        return True
