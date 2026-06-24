from config.config import LOGIN_URL
from pages.login_page import LoginPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_83_password_visibility_toggle(page):

    # ==========================
    # OPEN LOGIN PAGE
    # ==========================
    page.goto(LOGIN_URL)

    page.wait_for_timeout(3000)

    # ==========================
    # ENTER PASSWORD
    # ==========================
    password_input = page.locator(
        "input[type='password']"
    )

    test_password = "Test@123"

    password_input.fill(test_password)

    page.wait_for_timeout(1000)

    # ==========================
    # VERIFY EYE ICON EXISTS
    # ==========================
    eye_icon = page.locator(
        "svg"
    ).last

    assert eye_icon.is_visible(), \
        "Eye icon is not visible"

    print("Eye icon is visible")

    # ==========================
    # CLICK EYE ICON
    # ==========================
    eye_icon.click(force=True)

    page.wait_for_timeout(1000)

    # ==========================
    # VERIFY PASSWORD VISIBLE
    # ==========================
    visible_password = page.locator(
        "input[type='text']"
    )

    assert visible_password.is_visible(), \
        "Password not visible after clicking Eye icon"

    print("Password visible successfully")

    # ==========================
    # CLICK EYE ICON AGAIN
    # ==========================
    eye_icon.click(force=True)

    page.wait_for_timeout(1000)

    # ==========================
    # VERIFY PASSWORD MASKED
    # ==========================
    hidden_password = page.locator(
        "input[type='password']"
    )

    assert hidden_password.is_visible(), \
        "Password not masked after second click"

    print("Password masked successfully")

    print(
        "PASS: Password visibility toggle working correctly."
    )