import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_frame_2.app import App
from test_frame_2.black_handle import black_wrapper, BlackList


class BasePage:
    # 初始化driver和black list
    def __init__(self):
        self.driver = App().driver
        self.black_list = BlackList().black_list

    def screenshot(self, pic_path):
        return self.driver.save_screenshot(pic_path)

    def allure_add_screenshot(self, pic_path, pic_name):
        with open(pic_path, 'rb') as f:  # 图片，不需要加uft-8 打开图片用rb模式binary mode
            picture_data = f.read()
        allure.attach(picture_data, name=pic_name, attachment_type=allure.attachment_type.PNG)

    # 设计模式：代理模式，装饰器模式
    # 装饰器 find 出现弹窗 click
    @black_wrapper
    # @BlacksHandle
    def find(self, by, locator):
        # self.driver.save_screenshot("tmp.png")
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, content):
        self.find(by, locator).send_keys(content)

    # 滑动查找方式一
    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                      'scrollable(true).instance(0)).'
                                                                      'scrollIntoView(new UiSelector().'
                                                                      f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    # 滑动查找方式二
    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles = self.finds(by, locator)
        # 不停滑动直到找到位置
        while len(eles) == 0:
            # 滑动
            self.driver.swipe(0, 600, 0, 400)
            eles = self.finds(by, locator)
        self.driver.implicitly_wait(10)
        return eles[0]

    def swip_find_click(self, by, locator):
        self.swip_find(by, locator).click()

    def find_send_keys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_until_exist(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def wait_until_not_exist(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until_not(wait_ele_for)

    def get_toast_text(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

    # todo:basepage开始了无限膨胀
    # utf-8编码,为什么会出现乱码,如何处理: 为了统一不同语言编码到utf-8
    def key_value_step_yaml(self, yaml_path):
        FIND = 'find'
        ACTION = 'action'
        FIND_AND_CLICK = 'find_and_click'
        SEND = 'send'
        CONTENT = 'content'
        with open(yaml_path, 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
        # step: find, action
        for step in data:
            # 关键字可变问题:设置类常量
            xpath = step.get(FIND)
            action = step.get(ACTION)
            # 函数调用
            if action == FIND_AND_CLICK:
                self.find_and_click(MobileBy.XPATH, xpath)
            elif action == SEND:
                content = step.get(CONTENT)  # 取出发送文本
                self.find_and_send(MobileBy.XPATH, xpath, content)

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()
