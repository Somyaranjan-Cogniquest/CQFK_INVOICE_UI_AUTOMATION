from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_58_verify_logout_option_visible(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # CLICK PROFILE ICON
    # ==========================
    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.wait_for(state="visible")
    profile_icon.click()

    page.wait_for_timeout(2000)

    # ==========================
    # VERIFY LOGOUT OPTION
    # ==========================
    logout_option = page.locator("text=Logout")

    assert logout_option.is_visible(), \
        "Logout option is not visible in profile menu"

    print("Logout option is visible")

    # ==========================
    # OPTIONAL VERSION CHECK
    # ==========================
    version_text = page.locator("text=/v\\d+\\.\\d+/")

    if version_text.count() > 0:
        print("Version displayed:", version_text.first.text_content())
    else:
        print("Version not displayed")

    print("TC_58 Passed")

