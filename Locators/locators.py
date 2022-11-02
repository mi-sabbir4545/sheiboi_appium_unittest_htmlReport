from appium.webdriver.common.appiumby import AppiumBy


class EnglishLanguage:
    # signup
    engLanguage_ID = (AppiumBy.ID, "raven.reader:id/radioButtonEnglish")
    nextbutton_ID = (AppiumBy.ID, "raven.reader:id/nextButton")


class Login:
    clickloginbutton_ID = (AppiumBy.ID, "raven.reader:id/loginButton")
    emailaddress_ID = (AppiumBy.ID, "raven.reader:id/emailAddress")
    password_ID = (AppiumBy.ID, "raven.reader:id/password")
    submitbutton_ID = (AppiumBy.ID, "raven.reader:id/emailPassSubmitButton")


class HomeBar:
    homebutton_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")
    clickhomeicon_XPATH = (AppiumBy.XPATH,
                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.CheckedTextView")
    recent_release_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Recent Release')]")
    mylibrary_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'My Library')]")
    bookStore_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Book Store')]")
    faq_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'FAQ')]")
    info_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Info')]")
    walletRecharge_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Wallet Recharge')]")
    feedback_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Feedback')]")
    settings_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Settings')]")
    profilebutton_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Profile')]")


class Search:
    searchbutton_XPATH = (AppiumBy.ID, "raven.reader:id/menu_search")
    searchopt_ID = (AppiumBy.ID, "raven.reader:id/search_src_text")


class ClickBOOK:
    clickonbook_XPATH = (AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")
    addtocart_XPATH = (AppiumBy.ID, "raven.reader:id/cartBook")
    viewCart_XPATH = (AppiumBy.ID, "raven.reader:id/tv_add_shopping_cart_counter")


class Logout:
    logout_XPATH = (AppiumBy.XPATH, "//*[contains(@text,'Logout')]")
