from zakaz_ua.pages.base_page import BasePage

class MainPagelocators:
    CATEGORY_BUTTON = "//button[contains(@class, 'CategoriesMenuButton__inner')]"
    BBQ_CATEGORY_BUTTON = "//ul[@data-testid='categoriesMenuNav']//a[contains(@href, '/bbq-season-zakaz/')]"
    ACCOUNT_NAVIGATOR = "//div[@data-marker='account navigation']"
    LIST_MENU = "(//p[@class='AccountNavigationItem__text css-1sxve9s'])[6]"
    LIKE_BUTTON = "//button[@class='FavoriteButton css-13hb15a']"

class MainPage(BasePage):
    def click_category_button(self):
        self.page.click(MainPagelocators.CATEGORY_BUTTON)

    def click_bbq_button(self):
        self.page.click(MainPagelocators.BBQ_CATEGORY_BUTTON)

    def open_bbq_category(self):
        self.click_category_button()
        self.click_bbq_button()

    def open_account_navigator(self):
        self.page.hover(MainPagelocators.ACCOUNT_NAVIGATOR)

    def click_to_list_menu(self):
        self.page.click(MainPagelocators.LIST_MENU)

    def open_list_menu(self):
        self.open_account_navigator()
        self.page.wait_for_timeout(500)
        self.click_to_list_menu()

        #remove like
    def remove_like(self):
        self.page.click(MainPagelocators.LIKE_BUTTON)




