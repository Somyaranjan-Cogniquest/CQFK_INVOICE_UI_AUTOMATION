from pages.login_page import LoginPage
from test_data.test_data import USERNAME, PASSWORD
from config.config import LOGIN_URL
from playwright.sync_api import expect

def test_TC_03_invalid_username(page):

    # Step 1: Open login page
    page.goto(LOGIN_URL)

    # Step 2: Create login object
    login = LoginPage(page)

    # Step 3: Enter invalid username + valid password
    login.enter_username("wrong_user@example.com")
    login.enter_password(PASSWORD)

    # Step 4: Click login
    login.click_login()

    # Step 5: Verify error message
    error_msg = page.locator(
    "text=/User not found|Invalid credentials|Internal Server Error/i"
)

    expect(error_msg).to_be_visible()