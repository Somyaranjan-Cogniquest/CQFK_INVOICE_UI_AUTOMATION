from pages.login_page import LoginPage
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

import pytest

@pytest.mark.regression
def test_TC_17_trim_whitespace_in_username(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)

    username_with_spaces = f"   {USERNAME}   "

    login.login(username_with_spaces, PASSWORD)

    page.wait_for_timeout(5000)

    assert "dashboard" in page.url.lower()