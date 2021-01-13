from test_frame_1.page.pre_page import PrePage


class Search(PrePage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxx")
        self.basepage.key_value_step_yaml("../page/search.yaml")
        return True
