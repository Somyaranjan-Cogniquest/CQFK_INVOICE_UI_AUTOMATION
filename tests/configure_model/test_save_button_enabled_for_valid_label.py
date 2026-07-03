from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_006_verify_save_button_enabled_for_valid_label(page):

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
    # ENTER VALID LABEL
    # ==================================
    label_field = page.locator(
        "input[placeholder='Type data field']"
    ).first

    label_field.fill("AB")

    page.wait_for_timeout(1000)

    print("Entered Label : AB")

    # ==================================
    # VERIFY SAVE BUTTON ENABLED
    # ==================================
    save_btn = page.get_by_role(
        "button",
        name="Save"
    )

    assert save_btn.is_enabled(), \
        "Save button is still disabled after entering 2 characters"

    print(
        "PASS : Save button became enabled "
        "after entering at least 2 characters"
    )