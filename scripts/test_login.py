import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("login_data.yaml","test_login"))
    def test_login(self,args):
        # 解析
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 点击我的
        self.page.home.click_me_button()
        # 点击已有账号去登录
        self.page.to_login.click_to_login()
        # 输入用户名
        self.page.login.input_username(username)
        # 输入密码
        self.page.login.input_password(password)
        # 点击登录
        self.page.login.click_login()

        if toast is None:
            assert self.page.neckname.get_nick_name() == username
        else:
            assert self.page.login.is_toast_exist(toast)
