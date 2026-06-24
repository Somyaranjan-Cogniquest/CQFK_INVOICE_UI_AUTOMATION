from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_81_logout_invalidates_session_across_tabs(page):

    # ==========================
    # LOGIN IN TAB 1
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN DOCUMENT DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # Get browser context
    context = page.context

    # ==========================
    # TAB 2
    # ==========================
    tab2 = context.new_page()

    tab2.goto(page.url)

    tab2.wait_for_timeout(5000)

    print("Tab 2 opened successfully")

    # ==========================
    # TAB 1 LOGOUT
    # ==========================
    page.bring_to_front()

    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.click(force=True)

    page.wait_for_timeout(2000)

    page.get_by_text("Logout").click()

    page.wait_for_timeout(5000)

    assert "login" in page.url.lower(), \
        "Tab 1 not redirected to Login page"

    print("Logout successful from Tab 1")

    # ==========================
    # REFRESH TAB 2
    # ==========================
    tab2.bring_to_front()

    tab2.reload()

    tab2.wait_for_timeout(5000)

    # ==========================
    # VERIFY SESSION INVALIDATED
    # ==========================
    assert "login" in tab2.url.lower(), \
        "Session still active in Tab 2 after logout"

    print(
        "PASS: Refreshing Tab 2 redirected user to Login page."
    )