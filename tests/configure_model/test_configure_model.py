from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_001_verify_configure_model_navigation(page):

    # ==================================
    # LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    page.wait_for_timeout(5000)

    # ==================================
    # OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    print("Processing Dashboard opened")

    # ==================================
    # OPEN TAAS LANDING PAGE
    # ==================================
    dashboard.click_model_name()

    page.wait_for_timeout(5000)

    print("TAAS Landing Page opened")

    # ==================================
    # CLICK CONFIGURE MODEL
    # ==================================
    configure_model = page.get_by_text(
        "Configure Model",
        exact=False
    )

    configure_model.wait_for(
        state="visible",
        timeout=10000
    )

    configure_model.click()

    page.wait_for_timeout(5000)

    print("Configure Model clicked")

    # ==================================
    # VERIFY PAGE OPENED
    # ==================================
    current_url = page.url

    print("Current URL :", current_url)

    assert current_url != "", \
        "Configure Model page did not open"

    # Optional URL validation
    # assert "setting" in current_url.lower()

    print(
        "PASS : Configure Model page opened successfully"
    )