from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_005_verify_empty_label_validation(page):

    # ==================================
    # LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

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

    print("Configure Model page opened")

    # ==================================
    # OPEN ADD NEW SECTION PANEL
    # ==================================
    page.get_by_text(
        "Add new section",
        exact=False
    ).click()

    page.wait_for_timeout(3000)

    print("Add New Section panel opened")

    # ==================================
    # VERIFY SAVE BUTTON DISABLED
    # ==================================
    save_btn = page.get_by_role(
        "button",
        name="Save"
    )

    assert save_btn.is_disabled(), \
        "Save button is enabled when Label is empty"

    print(
        "PASS : Save button remained disabled "
        "when Label field was empty"
    )