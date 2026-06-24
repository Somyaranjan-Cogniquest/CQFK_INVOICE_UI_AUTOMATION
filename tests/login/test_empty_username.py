from pages.login_page import LoginPage
from config.config import LOGIN_URL
from test_data.test_data import PASSWORD

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_04_empty_username(page):

    # Open Login Page
    page.goto(LOGIN_URL)

    # Enter password only
    login = LoginPage(page)
    login.enter_password(PASSWORD)

    # Click Login
    login.click_login()

    # Verify validation message
    assert page.locator(
        "p.error-msg",
        has_text="Email is required"
    ).is_visible()