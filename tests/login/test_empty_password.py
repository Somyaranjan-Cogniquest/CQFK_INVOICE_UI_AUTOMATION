from pages.login_page import LoginPage
from config.config import LOGIN_URL
from test_data.test_data import USERNAME

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_05_empty_password(page):

    # Open Login Page
    page.goto(LOGIN_URL)

    # Enter username only
    login = LoginPage(page)
    login.enter_username(USERNAME)

    # Click Login
    login.click_login()

    # Verify validation message
    assert page.locator(
        "p.error-msg",
        has_text="Password is required"
    ).is_visible()