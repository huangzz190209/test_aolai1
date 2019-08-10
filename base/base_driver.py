# from appium import webdriver
#
# def init_driver():
#     desired_caps = dict()
#     # 设备信息
#     desired_caps['platfornName'] = 'Android'
#     desired_caps['platformVersion'] = '5'
#     desired_caps['deviceName'] = '192.168.56.101:5555'
#     #app信息
#     desired_caps['appPackage'] = 'com.yunmall.lc'
#     desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
#     #获取tosat
#     desired_caps['automationName'] = 'Uiautomator2'
#     # 重置
#     desired_caps['noReset'] = False
#
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#     return driver

from appium import webdriver


def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'

    desired_caps['automationName'] = 'Uiautomator2'
    # 不重置应用
    desired_caps['noReset'] = False

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
