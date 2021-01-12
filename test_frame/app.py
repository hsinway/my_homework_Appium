from appium import webdriver

from test_frame.base_page import BasePage
from test_frame.page.main import Main


class App(BasePage):
    def start(self):
        if self.driver is None:
            # 定义一个字典
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
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(5)

        return self  # self其实就是实例对象本身，那么return self 就是返回实例对象本身,用于链式调用,连续调用

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self) -> Main:
        return Main(self.driver)

    def quit(self):
        self.driver.quit()
