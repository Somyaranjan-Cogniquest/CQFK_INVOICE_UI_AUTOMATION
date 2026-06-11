from pages.login_page import LoginPage
from test_data.test_data import USERNAME
from config.config import LOGIN_URL

def test_TC_02_invalid_password(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.enter_username(USERNAME)
    login.enter_password("wrong_password")
    login.click_login()

    error_msg = page.get_by_role("alert")
    error_msg.wait_for(timeout=5000)

    assert "Invalid credentials" in error_msg.inner_text()