from test_frame_2.page.pre_page import PrePage


class Search(PrePage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxx")
        self.basepage.key_value_step_yaml("../file/search.yaml")
        return True
