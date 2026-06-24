from pages.login_page import LoginPage
from test_data.test_data import PASSWORD
from config.config import LOGIN_URL

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_03_invalid_username(page):

    # Step 1: Open login page
    page.goto(LOGIN_URL)

    # Step 2: Create login object
    login = LoginPage(page)

    # Step 3: Enter invalid username + valid password
    login.enter_username(
        "wrong_user@example.com"
    )

    login.enter_password(
        PASSWORD
    )

    # Step 4: Click login
    login.click_login()

    # Step 5: Verify error message
    error_msg = page.get_by_role(
        "alert"
    )

    error_msg.wait_for(
        timeout=5000
    )

    actual_message = (
        error_msg.inner_text().strip()
    )

    print(
        "Actual Error Message :",
        actual_message
    )

    assert (
        actual_message
        == "Invalid username or password"
    )

    print(
        "PASS : Invalid username error displayed successfully"
    )