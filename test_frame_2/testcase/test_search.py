import pytest

from test_frame_2.base_page import BasePage
from test_frame_2.page.main import Main


class TestSearch:
    """
    pytest test_search.py --alluredir ../allureresult --clean-alluredir
    allure serve ../allureresult
    """

    def setup(self):
        # 给basepage赋予对象BasePage，再传递给Main
        self.basepage = BasePage()
        self.app = Main(self.basepage)

    def teardown(self):
        # pass
        self.basepage.quit()

    # @pytest.mark.parametrize()
    def test_search(self):
        # App类里的start方法有return self,所以这里可以直接链式调用goto_main
        self.app.goto_market().goto_search().search()
