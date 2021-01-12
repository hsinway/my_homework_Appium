import logging

from appium.webdriver.common.mobileby import MobileBy

"""
可以通过level参数，设置不同的日志级别。当设置为高的日志级别时，低于此级别的日志不再打印。
五种日志级别按从低到高排序：
DEBUG < INFO < WARNING < ERROR < CRITICAL
例如level设置为DEBUG级别，所有的日志都会打印

pytest需要在pytest.ini中做配置才能实时显示log
log_cli = true
log_cli_level = INFO
"""
logging.basicConfig(level=logging.INFO)


class BlackList:
    def __init__(self):
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/ib_close']"),
                           (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
                           ]


# 不再使用base_page代表self,而是直接添加self标明
def black_wrapper(fun):
    def run(self, *args, **kwargs):
        # 封装弹窗处理
        try:
            # print(args)
            # 日志打印
            logging.info(f"start find: \nargs: {args} kwargs: {kwargs}")
            return fun(self, *args, **kwargs)  # 第一次尝试执行fun
        # 捕获元素没找到的异常
        except Exception as e:
            # 截图,方法在base_page里
            self.screenshot("../screenshot/popup.png")
            # 添加到allure报告里
            self.allure_add_screenshot("../screenshot/popup.png", "popup")
            # 获取黑名单
            black_list = BlackList().black_list
            # 遍历黑名单中的元素，进行处理
            for black_locator in black_list:
                eles = self.finds(*black_locator)
                # 黑名单元素被找到
                if len(eles) > 0:
                    # 对黑名单元素进行点击操作等，操作可以自由扩展
                    eles[0].click()
                    return fun(self, *args, **kwargs)  # 第二次执行fun
            raise e  # 没找到匹配的黑名单,抛出异常

    return run


# 用base_page代表self,fun中不再标明self
def black_wrapper_old(fun):
    def run(*args, **kwargs):
        base_page = args[0]  # 参数第一个self
        # 封装弹窗处理
        try:
            print(args)
            return fun(*args, **kwargs)  # 第一次尝试执行fun
        # 捕获元素没找到的异常
        except Exception as e:
            # 遍历黑名单中的元素，进行处理
            for black_locator in base_page.black_list:
                eles = base_page.finds(*black_locator)
                # 黑名单元素被找到
                if len(eles) > 0:
                    # 对黑名单元素进行点击操作等，操作可以自由扩展
                    eles[0].click()
                    return fun(*args, **kwargs)  # 第二次执行fun
            raise e  # 没找到匹配的黑名单,抛出异常

    return run
