from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_013_verify_add_new_field_ui(page):

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
    # OPEN ADD NEW FIELD PANEL
    # ==================================
    page.get_by_text(
        "Add new field",
        exact=False
    ).click()

    page.wait_for_timeout(3000)

    print("Add New Field panel opened")

    # ==================================
    # VERIFY LABEL FIELD
    # ==================================
    label_field = page.locator(
        "input[placeholder='Type data field']"
    )

    assert label_field.is_visible(), \
        "Label field is not visible"

    print("Label field displayed")

    # ==================================
    # VERIFY PRESENTATION TYPE
    # ==================================
    presentation_type = page.get_by_text(
        "Presentation type",
        exact=False
    )

    assert presentation_type.is_visible(), \
        "Presentation Type not visible"

    print("Presentation Type displayed")

    # ==================================
    # VERIFY DATA TYPE
    # ==================================
    data_type = page.get_by_text(
        "Data type",
        exact=False
    )

    assert data_type.is_visible(), \
        "Data Type not visible"

    print("Data Type displayed")

    # ==================================
    # VERIFY REQUIRED TOGGLE
    # ==================================
    required = page.get_by_text(
        "Required",
        exact=False
    )

    assert required.is_visible(), \
        "Required option not visible"

    print("Required option displayed")

    # ==================================
    # VERIFY VISIBLE TOGGLE
    # ==================================
    visible = page.get_by_text(
        "Visible",
        exact=False
    )

    assert visible.is_visible(), \
        "Visible option not visible"

    print("Visible option displayed")

    print(
        "PASS : Label, Presentation Type, "
        "Data Type, Required and Visible "
        "options were displayed successfully."
    )