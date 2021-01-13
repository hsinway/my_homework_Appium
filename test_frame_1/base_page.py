import allure
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_frame_1.black_handle import black_wrapper, BlackList


class BasePage:
    # base 类中用init初始化driver,则继承它的子类都会调用,加上注解WebDriver,则输入driver会提示引用对应的方法
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator_qiyeweixin'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"  # 设为True后则不会初始化之前的操作，例如之前操作关闭了更新提示，或者有登录信息，True则不会清除上述操作或者缓存，信息
        # desired_caps['dontStopAppOnReset'] = True  # 首次启动的时候不停止APP：run之前app停留在哪个页面就从那个页面执行，执行完不退出app
        desired_caps['skipDeviceInitialization'] = "true"  # 跳过初始化过程
        desired_caps['unicodeKeyboard'] = "true"  # 开启unicodte输入,方便输入中文
        desired_caps['resetKeyboard'] = "true"  # 重设unicodeKeyboard
        desired_caps['ensureWebviewsHavePages'] = "true"  # 支持页面动态刷新
        desired_caps['settings[waitForIdleTimeout]'] = 10  # 设置页面等待页面加载完成到空闲状态的时间,默认为10秒,这里设置为0秒
        desired_caps['skipServerInstallation'] = "true"  # 跳过 uiautomator2 server的安装
        # 关键 localhost:4723 本机ip:server端口
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
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
