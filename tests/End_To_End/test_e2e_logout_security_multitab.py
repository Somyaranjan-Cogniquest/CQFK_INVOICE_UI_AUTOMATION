from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_E2E_09_logout_security_multitab(page):

    # ==================================
    # STEP 1 : LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    print("Login successful")

    # ==================================
    # STEP 2 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    protected_url = page.url

    print("Protected URL:", protected_url)

    # ==================================
    # STEP 3 : OPEN SECOND TAB
    # ==================================
    context = page.context

    tab2 = context.new_page()

    tab2.goto(protected_url)

    dashboard2 = DashboardPage(tab2)

    dashboard2.wait_for_table()

    print("Second tab opened successfully")

    # ==================================
    # STEP 4 : LOGOUT FROM TAB 1
    # ==================================
    page.bring_to_front()

    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.click(force=True)

    page.wait_for_timeout(2000)

    page.get_by_text(
        "Logout"
    ).click(force=True)

    page.wait_for_timeout(3000)

    assert "login" in page.url.lower(), \
        "User not redirected to Login page"

    print("Logout successful")

    # ==================================
    # STEP 5 : REFRESH TAB 2
    # ==================================
    tab2.bring_to_front()

    tab2.reload()

    page.wait_for_timeout(5000)

    assert "login" in tab2.url.lower(), \
        "Session still active in second tab"

    print(
        "Second tab redirected to Login page"
    )

    # ==================================
    # STEP 6 : TRY DIRECT URL ACCESS
    # ==================================
    tab2.goto(protected_url)

    page.wait_for_timeout(3000)

    assert "login" in tab2.url.lower(), \
        "Protected URL accessible after logout"

    print(
        "Protected URL blocked successfully"
    )

    # ==================================
    # STEP 7 : BROWSER BACK BUTTON
    # ==================================
    tab2.go_back()

    page.wait_for_timeout(3000)

    assert "login" in tab2.url.lower(), \
        "Back button restored session"

    print(
        "Back button did not restore session"
    )

    print(
        "PASS : E2E_09 Logout + Security + Multi-Tab Invalidation"
    )