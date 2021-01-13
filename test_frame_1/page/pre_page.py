from test_frame_1.base_page import BasePage


# 这里PrePage只是初始化一个basepage变量，作为Main，Market之间传递的作用
class PrePage:
    def __init__(self, basepage: BasePage):  # 可以声明basepage类型，也可以不声明
        self.basepage = basepage
