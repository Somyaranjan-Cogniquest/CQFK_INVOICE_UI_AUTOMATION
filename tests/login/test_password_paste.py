from pages.login_page import LoginPage
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

def test_TC_18_password_field_paste_allowed(page):

    # Open Login Page
    page.goto(LOGIN_URL)

    # Enter Username
    login = LoginPage(page)
    login.enter_username(USERNAME)

    # Paste Password into Password Field
    page.locator('input[type="password"]').fill(PASSWORD)

    # Verify password is masked
    assert page.locator('input[type="password"]').get_attribute("type") == "password"

    # Click Login
    login.click_login()

    page.wait_for_timeout(5000)

    # Verify Login Success
    assert "dashboard" in page.url.lower()