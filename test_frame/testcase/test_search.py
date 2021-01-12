import pytest

from test_frame.app import App


class TestSearch:
    """
    pytest test_search.py --alluredir ../allureresult --clean-alluredir
    allure serve ../allureresult
    """

    def setup(self):
        self.app = App()
        # self.app.start()

    # @pytest.mark.parametrize()
    def test_search(self):
        # App类里的start方法有return self,所以这里可以直接链式调用goto_main
        self.app.start().goto_main().goto_market().goto_search().search()
