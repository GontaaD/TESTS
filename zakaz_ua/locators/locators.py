class MainPagelocators:
    LOGIN_BUTTON = "//button[contains(@class, 'LoginButton css-hnx7nu')]"
    CATEGORY_BUTTON = "//button[contains(@class, 'CategoriesMenuButton__inner')]"
    BBQ_CATEGORY_BUTTON = "//ul[@data-testid='categoriesMenuNav']//a[contains(@href, '/bbq-season-zakaz/')]"

class LoginPagelocators:
    NUMBER_INPUT = "//input[@class='form-control ']"
    PASSWORD_INPUT = "//input[@class='Input__field']"
    LOGIN_BUTTON = "//button[@class='css-xdkem']"

class BBQCategoryPageLocators:
    HEART_BUTTON = "(//div[@data-marker='Products List']//i[contains(@class, 'icon-heart')])[1]"
    PRODUCT_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"
    ACCOUNT_NAVIGATOR = "//div[@data-marker='account navigation']"
    HEART_LIST_BUTTON = "//i[@class='icon-heart-full AccountNavigationItem__icon css-15hz7qx']"

class HeartListPageLocators:
    PRODUCT_IN_LIST_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"

class LoginNumberAndPasswors:
    NUMBER = "997952094"
    PASSWORD = "198595"