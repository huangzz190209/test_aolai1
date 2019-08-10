from page.home_page import HomePage
from page.login_page import LoginPage
from page.neck_name_page import NeckNamePage
from page.to_login_page import ToLoginPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)
    @property
    def to_login(self):
        return ToLoginPage(self.driver)
    @property
    def login(self):
        return LoginPage(self.driver)
    @property
    def neckname(self):
        return NeckNamePage(self.driver)


