from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_008_verify_spaces_only_validation(page):

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
    # ENTER SPACES ONLY
    # ==================================
    label_field = page.locator(
        "input[placeholder='Type data field']"
    ).first

    label_field.fill("     ")

    page.wait_for_timeout(1000)

    print("Entered spaces in Label field")

    # ==================================
    # VERIFY SAVE BUTTON DISABLED
    # ==================================
    save_btn = page.get_by_role(
        "button",
        name="Save"
    )

    assert save_btn.is_disabled(), \
        "Save button is enabled for spaces only input"

    print(
        "Save button remained disabled"
    )

    # ==================================
    # VERIFY VALIDATION MESSAGE
    # ==================================
    validation_msg = page.get_by_text(
        "Please enter",
        exact=False
    )

    assert validation_msg.is_visible(), \
        "Validation message not displayed"

    print(
        "PASS : Validation message displayed "
        "for spaces only input"
    )