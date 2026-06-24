from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_E2E_11_cross_tab_session_invalidation(page):

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
    # STEP 2 : TAB 1 -> DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    print("Dashboard opened in Tab 1")

    # ==================================
    # STEP 3 : OPEN TAB 2
    # ==================================
    context = page.context

    tab2 = context.new_page()

    tab2.goto(page.url)

    dashboard2 = DashboardPage(tab2)

    dashboard2.click_processing_dashboard()

    dashboard2.wait_for_table()

    print("Processing Dashboard opened in Tab 2")

    # ==================================
    # STEP 4 : LOGOUT FROM TAB 1
    # ==================================
    page.bring_to_front()

    profile_icon = page.locator(
        "div[style*='border-radius: 50%']"
    ).first

    profile_icon.click(force=True)

    page.get_by_text(
        "Logout"
    ).click(force=True)

    page.wait_for_timeout(3000)

    assert "login" in page.url.lower(), \
        "Logout failed in Tab 1"

    print("Logout successful from Tab 1")

    # ==================================
    # STEP 5 : REFRESH TAB 2
    # ==================================
    tab2.bring_to_front()

    print("Refreshing Tab 2")

    tab2.reload()

    tab2.wait_for_load_state(
        "networkidle"
    )

    page.wait_for_timeout(3000)

    print("Tab 2 refreshed")

    # ==================================
    # STEP 6 : VERIFY SESSION INVALIDATED
    # ==================================
    assert "login" in tab2.url.lower(), \
        f"Session still active in Tab 2 : {tab2.url}"

    print(
        "Tab 2 redirected to Login page"
    )

    # ==================================
    # STEP 7 : VERIFY PROTECTED PAGE BLOCKED
    # ==================================
    assert "/document" not in tab2.url.lower(), \
        "Protected page still accessible"

    print(
        "Protected page access blocked"
    )

    print(
        "PASS : E2E_11 Cross Tab Session Invalidation"
    )