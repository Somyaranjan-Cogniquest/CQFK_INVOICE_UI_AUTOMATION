from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

from pages.login_page import LoginPage
from playwright.sync_api import expect

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_62_verify_profile_dropdown_closes_on_outside_click(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN PROFILE DROPDOWN
    # ==========================
    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.click()

    page.wait_for_timeout(2000)

    # Verify Logout option visible
    logout_option = page.get_by_text("Logout")

    expect(logout_option).to_be_visible()

    print("Profile dropdown opened successfully")

    # ==========================
    # CLICK OUTSIDE DROPDOWN
    # ==========================
    page.mouse.click(50, 50)

    page.wait_for_timeout(2000)

    # ==========================
    # VERIFY DROPDOWN CLOSED
    # ==========================
    expect(logout_option).not_to_be_visible()

    print("Profile dropdown closed successfully after outside click")