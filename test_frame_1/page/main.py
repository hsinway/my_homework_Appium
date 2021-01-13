from test_frame_1.page.market import Market
from test_frame_1.page.pre_page import PrePage


# 继承自PrePage以及它的basepage参数
class Main(PrePage):
    def goto_market(self):
        # 因为执行目录是test_search文件,所以要先..到父级目录再找文件
        self.basepage.key_value_step_yaml("../page/main.yaml")
        return Market(self.basepage)  # Market也继承PrePage，basepage将会被赋予一个对象，因此传递给Market
