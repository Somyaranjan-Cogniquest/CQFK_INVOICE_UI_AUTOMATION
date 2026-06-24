from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_61_verify_direct_url_access_blocked_after_logout(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # LOGOUT
    # ==========================
    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.click()

    page.wait_for_timeout(2000)

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
        "User was not redirected to Login page"

    # ==========================
    # TRY DIRECT DASHBOARD URL
    # ==========================
    page.goto(
        "https://cqfk-invoice.cogniquest.ai/InvIDPApi/dashboard"
    )

    page.wait_for_timeout(5000)

    assert "login" in page.url.lower(), \
        "Dashboard accessible after logout"

    print("Dashboard access blocked")

    # ==========================
    # TRY DIRECT DOCUMENT URL
    # ==========================
    page.goto(
        "https://cqfk-invoice.cogniquest.ai/InvIDPApi/document"
    )

    page.wait_for_timeout(5000)

    assert "login" in page.url.lower(), \
        "Document page accessible after logout"

    print("Document page access blocked")

    print("TC_61 Passed - Direct URL access blocked after logout")