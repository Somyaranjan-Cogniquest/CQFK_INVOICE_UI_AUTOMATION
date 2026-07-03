from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_012_verify_add_new_field_button(page):

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

    # ==================================
    # OPEN TAAS LANDING PAGE
    # ==================================
    dashboard.click_model_name()

    page.wait_for_timeout(5000)

    # ==================================
    # OPEN CONFIGURE MODEL
    # ==================================
    page.get_by_text(
        "Configure Model",
        exact=False
    ).click()

    page.wait_for_timeout(5000)

    print(
        "Configure Model page opened"
    )

    # ==================================
    # CLICK ADD NEW FIELD
    # ==================================
    page.get_by_text(
        "Add new field",
        exact=False
    ).click()

    page.wait_for_timeout(3000)

    print(
        "Clicked Add New Field"
    )

    # ==================================
    # VERIFY ADD NEW FIELD PANEL OPENED
    # ==================================
    label_input = page.locator(
        "input[placeholder='Type data field']"
    )

    assert label_input.is_visible(), \
        "Add New Field panel did not open"

    print(
        "PASS : Add New Field panel "
        "opened successfully"
    )