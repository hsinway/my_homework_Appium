from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class Test_Wechat:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator_qiyeweixin'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = "true"  # 设为True后则不会初始化之前的操作，例如之前操作关闭了更新提示，或者有登录信息，True则不会清除上述操作或者缓存，信息
        # desired_caps['dontStopAppOnReset'] = True  # 首次启动的时候不停止APP：run之前app停留在哪个页面就从那个页面执行，执行完不退出app
        desired_caps['skipDeviceInitialization'] = "true"  # 跳过初始化过程
        desired_caps['unicodeKeyboard'] = "true"  # 开启unicodte输入,方便输入中文
        desired_caps['resetKeyboard'] = "true"  # 重设unicodeKeyboard
        desired_caps['ensureWebviewsHavePages'] = "true"  # 重设unicodeKeyboard
        desired_caps['settings[waitForIdleTimeout]'] = 0  # 设置页面等待页面加载完成到空闲状态的时间,默认为10秒,这里设置为0秒
        desired_caps['skipServerInstallation'] = "true"  # 跳过 uiautomator2 server的安装
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 添加回到首页操作,或者去掉desired capabilities里的dontStopAppOnReset属性
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_data(self):
        # 进入工作台，resource-id 后缀dqn代表可变id 不可以作为查找定位元素
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动查找打卡标签的元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 这里用contains是因为页面上时间变化，第几次打开的数字也变化只能模糊匹配
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # sleep(2)
        # 获取页面全部元素
        print(self.driver.page_source)
        # 隐式等待要触发find element等方法才会触发,这里要加显示等待,否则page_source不会立刻拿到所有的元素
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
