from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # base 类中用init初始化driver,则继承它的子类都会调用,加上注解WebDriver,则输入driver会提示引用对应的方法
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

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
