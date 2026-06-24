from config.config import LOGIN_URL
from locators.login_locators import LoginLocators

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_06_empty_username_password(page):

    page.goto(LOGIN_URL)

    page.click(LoginLocators.LOGIN_BUTTON)

    error_msg = page.locator(LoginLocators.EMPTY_BOTH_ERROR)

    assert error_msg.is_visible()
    assert error_msg.text_content() == "*Email and Password are required"