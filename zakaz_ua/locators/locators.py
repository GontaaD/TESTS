class MainPagelocators:
    CATEGORY_BUTTON = "//button[contains(@class, 'CategoriesMenuButton__inner')]"
    BBQ_CATEGORY_BUTTON = "//ul[@data-testid='categoriesMenuNav']//a[contains(@href, '/bbq-season-zakaz/')]"
    ACCOUNT_NAVIGATOR = "//div[@data-marker='account navigation']"
    LIST_MENU = "(//p[@class='AccountNavigationItem__text css-1sxve9s'])[6]"

class LoginPagelocators:
    LOGIN_BUTTON = "//button[contains(@class, 'LoginButton css-hnx7nu')]"
    NUMBER_INPUT = "//input[@class='form-control ']"
    PASSWORD_INPUT = "//input[@class='Input__field']"
    LOGIN_APPLY = "//button[@class='css-xdkem']"

class BBQCategoryPageLocators:
    HEART_BUTTON = "(//div[@data-marker='Products List']//i[contains(@class, 'icon-heart')])[1]"
    PRODUCT_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"
    ACCOUNT_NAVIGATOR = "//div[@data-marker='account navigation']"
    HEART_LIST_BUTTON = "//i[@class='icon-heart-full AccountNavigationItem__icon css-15hz7qx']"
    MIN_PRICE_FILTER = "//input[@data-testid='price-min']"
    MAX_PRICE_FILTER = "//input[@data-testid='price-max']"
    START_PRODUCT_PRICE = "//span[@class='PricesRange__start']"
    END_PRODUCT_PRICE = "//span[@class='PricesRange__end']"
    FILTER_APPLY_BUTTON = "//button[@data-marker='Filter Price OK']"
    PRICE_BLOCK = "//span[@data-sentry-component='PriceRange']"

class HeartListPageLocators:
    PRODUCT_IN_LIST_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"

class LoginNumberAndPasswors:
    NUMBER = "997952094"
    PASSWORD = "198595"

class ListPageLocators:
    RENAME_BUTTON = "//button[@data-marker='Change name']"
    LIST = "(//div[@class='css-1o947s6'])[1]"
    INPUT_LIST_NAME = "//input[@data-marker='List name']"
    APPLY_LIST_NAME_BUTTON = "//button[@data-marker='Save']"
    LIST_NAME = "(//p[@class='css-7m85l7'])[2]"
