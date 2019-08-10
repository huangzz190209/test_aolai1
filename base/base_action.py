from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    #定位一个元素
    def find_element(self,feature,timeout=10,poll=1.0):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(feature[0],feature[1]))

    #定位多个元素
    def find_elements(self,feature,timeout = 10,poll = 1.0):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(feature[0],feature[1]))

    # 封装点击操作
    def click(self,feature):
        self.find_element(feature).click()
    #封装输入操作
    def input_text(self,feature,text):
        self.find_element(feature).send_keys(text)
    #清空输入
    def clear_input(self,feature):
        self.find_element(feature).clear()
    #获取元素文本信息
    def get_text(self,feature):
        return self.find_element(feature).text

    def is_toast_exist(self,toast):
        message_xpath = By.XPATH,"//*[contains(@text,%s)]" % toast
        try:
            self.find_element(message_xpath,5,0.1)
            return True
        except TimeoutException:
            return False









