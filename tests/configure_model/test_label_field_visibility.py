from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_004_verify_label_field_visibility(page):

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

    print("Configure Model page opened")

    # ==================================
    # CLICK ADD NEW SECTION
    # ==================================
    page.get_by_text(
        "Add new section",
        exact=False
    ).click()

    page.wait_for_timeout(3000)

    print("Add New Section panel opened")

    # ==================================
    # VERIFY LABEL TEXT
    # ==================================
    label_text = page.locator(
        "label:has-text('Label')"
    )

    assert label_text.is_visible(), \
        "Label text is not visible"

    print("Label text is visible")

    # ==================================
    # VERIFY LABEL TEXTBOX
    # ==================================
    label_textbox = page.locator(
        "input[placeholder='Type data field']"
    ).first

    assert label_textbox.is_visible(), \
        "Label textbox is not visible"

    print(
        "PASS : Label textbox was displayed successfully."
    )