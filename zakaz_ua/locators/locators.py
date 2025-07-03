class MainPagelocators:
    CATEGORY_BUTTON = "//button[contains(@class, 'CategoriesMenuButton__inner')]"
    BBQ_CATEGORY_BUTTON = "//ul[@data-testid='categoriesMenuNav']//a[contains(@href, '/bbq-season-zakaz/')]"
    ACCOUNT_NAVIGATOR = "//div[@data-marker='account navigation']"
    LIST_MENU = "(//p[@class='AccountNavigationItem__text css-1sxve9s'])[6]"
    LIKE_BUTTON = "//button[@class='FavoriteButton css-13hb15a']"

class LoginPagelocators:
    LOGIN_BUTTON = "//button[contains(@class, 'LoginButton css-hnx7nu')]"
    NUMBER_INPUT = "//input[@class='form-control ']"
    PASSWORD_INPUT = "//input[@class='Input__field']"
    LOGIN_APPLY = "//button[@class='css-xdkem']"

class BBQCategoryPageLocators:
    HEART_BUTTON = "(//div[@data-marker='Products List']//i[contains(@class, 'icon-heart')])[1]"
    PRODUCT_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"
    MIN_PRICE_FILTER = "//input[@data-testid='price-min']"
    MAX_PRICE_FILTER = "//input[@data-testid='price-max']"
    START_PRODUCT_PRICE = "//span[@class='PricesRange__start']"
    END_PRODUCT_PRICE = "//span[@class='PricesRange__end']"
    FILTER_APPLY_BUTTON = "//button[@data-marker='Filter Price OK']"
    PRICE_BLOCK = "//span[@data-sentry-component='PriceRange']"

class ListPageLocators:
    RENAME_BUTTON = "//button[@data-marker='Change name']"
    MY_CREATED_LIST = "(//div[@class='css-1o947s6'])[1]"
    RENAME_MY_CREATED_LIST = "//div[@class='css-aqrc7q']"
    INPUT_LIST_NAME = "//input[@data-marker='List name']"
    APPLY_LIST_NAME_BUTTON = "//button[@data-marker='Save']"
    MY_CREATED_LIST_NAME = "(//p[@class='css-7m85l7'])[2]"
    PRODUCT_IN_LIST_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"
    first_list_name = "Обрані"
    second_list_name = "лист123"
    FIRST_LIST_IN_CHANGE_LIST = "//*[text()='{0}']//ancestor::div[@class='css-1qx3rq8']".format(first_list_name)
    SECOND_LIST_IN_CHANGE_LIST = "//*[text()='{0}']//ancestor::div[@class='css-1l7o2vn']".format(second_list_name)
    SAVE_CHANGE_LIST_BUTTON = "//button[@data-marker='Save']"
    CHANGE_BUTTON = "//button[@data-marker='change']"