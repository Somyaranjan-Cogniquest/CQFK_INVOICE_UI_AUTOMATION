from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_60_verify_browser_back_after_logout(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN PROFILE MENU
    # ==========================
    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.click()

    page.wait_for_timeout(2000)

    # ==========================
    # LOGOUT
    # ==========================
    logout_btn = page.get_by_text(
        "Logout",
        exact=False
    )

    assert logout_btn.is_visible(), \
        "Logout option not visible"

    logout_btn.click()

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY LOGIN PAGE
    # ==========================
    assert "login" in page.url.lower(), \
        f"Not redirected to login page. URL: {page.url}"

    print("Logout successful")

    # ==========================
    # PRESS BROWSER BACK
    # ==========================
    page.go_back()

    page.wait_for_timeout(5000)

    print("URL after browser back:", page.url)

    # ==========================
    # VERIFY SESSION NOT RESTORED
    # ==========================
    assert "login" in page.url.lower(), \
        "User session restored after browser back"

    print("User remained logged out")