from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


def login_again(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    page.wait_for_timeout(5000)


def logout_and_verify(page):

    profile_icons = page.locator(
        "div[style*='border-radius: 50%']"
    )

    total_icons = profile_icons.count()

    print(
        f"Profile Icons Found : {total_icons}"
    )

    logout_clicked = False

    for i in range(total_icons):

        try:

            profile_icons.nth(i).click(
                force=True
            )

            page.wait_for_timeout(2000)

            logout_btn = page.get_by_text(
                "Logout"
            )

            if logout_btn.count() > 0:

                logout_btn.first.click(
                    force=True
                )

                logout_clicked = True

                break

        except Exception:

            continue

    assert logout_clicked, \
        "Logout option not found"

    page.wait_for_timeout(5000)

    assert "login" in page.url.lower(), \
        "User not redirected to Login page"

    print("Logout successful")


# MARKERS MUST BE HERE
@pytest.mark.smoke
@pytest.mark.regression
def test_TC_63_logout_from_all_major_pages(page):

    # your complete existing test code
    login_again(page)

    print("Testing Logout from Dashboard")

    logout_and_verify(page)

    # rest of your code unchanged