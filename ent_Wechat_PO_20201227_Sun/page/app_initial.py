from appium import webdriver

from ent_Wechat_PO_20201227_Sun.page.base_page import BasePage
from ent_Wechat_PO_20201227_Sun.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator_qiyeweixin'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['noReset'] = True  # 设为True后则不会初始化之前的操作，例如之前操作关闭了更新提示，或者有登录信息，True则不会清除上述操作或者缓存，信息
            # desired_caps['dontStopAppOnReset'] = True  # 首次启动的时候不停止APP：run之前app停留在哪个页面就从那个页面执行，执行完不退出app
            desired_caps['skipDeviceInitialization'] = "true"  # 跳过初始化过程
            desired_caps['unicodeKeyboard'] = "true"  # 开启unicodte输入,方便输入中文
            desired_caps['resetKeyboard'] = "true"  # 重设unicodeKeyboard
            desired_caps['ensureWebviewsHavePages'] = "true"  # 支持页面动态刷新
            desired_caps['settings[waitForIdleTimeout]'] = 0  # 设置页面等待页面加载完成到空闲状态的时间,默认为10秒,这里设置为0秒
            desired_caps['skipServerInstallation'] = "true"  # 跳过 uiautomator2 server的安装
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)

    def quit(self):
        self.driver.quit()
