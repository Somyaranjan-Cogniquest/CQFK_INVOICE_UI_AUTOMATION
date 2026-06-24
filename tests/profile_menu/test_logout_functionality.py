from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_TC_59_verify_logout(page):

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
    # VERIFY LOGOUT VISIBLE
    # ==========================
    logout_btn = page.get_by_text(
        "Logout",
        exact=False
    )

    assert logout_btn.is_visible(), \
        "Logout option is not visible"

    # ==========================
    # CLICK LOGOUT
    # ==========================
    logout_btn.click()

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY REDIRECT TO LOGIN
    # ==========================
    assert "login" in page.url.lower(), \
        f"Not redirected to login page. Current URL: {page.url}"

    print("Redirected URL:", page.url)

    # ==========================
    # VERIFY PROTECTED PAGE
    # CANNOT BE ACCESSED
    # ==========================
    page.goto(
        "https://cqfk-invoice.cogniquest.ai/InvIDPApi/document"
    )

    page.wait_for_timeout(5000)

    assert "login" in page.url.lower(), \
        "Protected page accessible after logout"

    print("Protected page blocked after logout")