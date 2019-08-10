from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NeckNamePage(BaseAction):
    #昵称
    nick_name = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    #点击已有账号去登陆
    def get_nick_name(self):
        return self.get_text(self.nick_name)