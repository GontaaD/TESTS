from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.list_page import ListPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.CheckTest_page import CheckTestPage
from zakaz_ua.pages.settings_page import SettingsPage
from zakaz_ua.pages.address_page import AddressPage
from page_wrapper import PageWrapper as Pgw

class PageMeneger:
    def __init__(self, page):
        self.page = page
        self.wrapper = Pgw(page)
        self.main_page = MainPage(page)
        self.bbq_page = BBQPage(page)
        self.list_page = ListPage(page)
        self.login_page = LoginPage(page)
        self.check_page = CheckTestPage(page)
        self.settings_page = SettingsPage(page)
        self.address_page = AddressPage(page)