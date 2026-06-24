from config.config import LOGIN_URL

import pytest

@pytest.mark.regression
def test_TC_85_password_value_retained_after_toggle(page):

    # ==========================
    # OPEN LOGIN PAGE
    # ==========================
    page.goto(LOGIN_URL)

    page.wait_for_timeout(3000)

    # ==========================
    # ENTER PASSWORD
    # ==========================
    password = "Test@123"

    password_field = page.locator(
        "input[type='password']"
    )

    password_field.fill(password)

    page.wait_for_timeout(1000)

    # Verify entered value
    assert password_field.input_value() == password

    # ==========================
    # EYE ICON
    # ==========================
    eye_icon = page.locator("svg").last

    assert eye_icon.is_visible(), \
        "Eye icon not visible"

    # ==========================
    # TOGGLE 1
    # ==========================
    eye_icon.click(force=True)

    page.wait_for_timeout(1000)

    visible_field = page.locator(
        "input[type='text']"
    )

    assert visible_field.input_value() == password, \
        "Password changed after first toggle"

    # ==========================
    # TOGGLE 2
    # ==========================
    eye_icon.click(force=True)

    page.wait_for_timeout(1000)

    hidden_field = page.locator(
        "input[type='password']"
    )

    assert hidden_field.input_value() == password, \
        "Password changed after second toggle"

    # ==========================
    # TOGGLE 3
    # ==========================
    eye_icon.click(force=True)

    page.wait_for_timeout(1000)

    visible_field = page.locator(
        "input[type='text']"
    )

    assert visible_field.input_value() == password, \
        "Password changed after third toggle"

    print(
        "PASS: Password value remains unchanged after multiple visibility toggles."
    )