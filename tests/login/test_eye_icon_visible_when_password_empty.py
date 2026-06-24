from config.config import LOGIN_URL

import pytest

@pytest.mark.regression
def test_TC_84_eye_icon_visible_when_password_empty(page):

    # ==========================
    # OPEN LOGIN PAGE
    # ==========================
    page.goto(LOGIN_URL)

    page.wait_for_timeout(3000)

    # ==========================
    # VERIFY PASSWORD FIELD EXISTS
    # ==========================
    password_field = page.locator(
        "input[type='password']"
    )

    assert password_field.is_visible(), \
        "Password field not visible"

    # ==========================
    # VERIFY PASSWORD FIELD EMPTY
    # ==========================
    assert password_field.input_value() == "", \
        "Password field is not empty"

    # ==========================
    # VERIFY EYE ICON VISIBLE
    # ==========================
    eye_icon = page.locator("svg").last

    assert eye_icon.is_visible(), \
        "Eye icon not visible when password field is empty"

    print(
        "PASS: Eye icon is visible even when password field is empty."
    )