from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_002_verify_data_fields_page_ui(page):

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
    # VERIFY DATA FIELDS PAGE
    # ==================================
    assert page.get_by_text(
        "Data fields",
        exact=False
    ).first.is_visible(), \
        "Data Fields header not visible"

    print("Data Fields header visible")

    # ==================================
    # VERIFY EXPORT BUTTON
    # ==================================
    assert page.get_by_text(
        "Export",
        exact=False
    ).is_visible(), \
        "Export button not visible"

    print("Export button visible")

    # ==================================
    # VERIFY INVOICE DETAILS SECTION
    # ==================================
    assert page.get_by_text(
        "InvoiceDetails",
        exact=False
    ).is_visible(), \
        "InvoiceDetails section not visible"

    print("InvoiceDetails section visible")

    # ==================================
    # VERIFY FIELD COUNT
    # ==================================
    field_badge = page.locator(
        "text=fields"
    ).first

    assert field_badge.is_visible(), \
        "Field count badge not visible"

    print(
        "Field badge:",
        field_badge.inner_text()
    )

    # ==================================
    # VERIFY FIELD CARDS
    # ==================================
    field_cards = page.locator(
        "div:has-text('SupplierName')"
    )

    assert field_cards.count() > 0, \
        "Field cards not displayed"

    print(
        f"Field cards found: "
        f"{field_cards.count()}"
    )

    # ==================================
    # VERIFY ADD NEW FIELD BUTTON
    # ==================================
    assert page.get_by_text(
        "Add new field",
        exact=False
    ).is_visible(), \
        "Add new field button not visible"

    print("Add new field button visible")

    # ==================================
    # VERIFY ADD NEW SECTION BUTTON
    # ==================================
    assert page.get_by_text(
        "Add new section",
        exact=False
    ).is_visible(), \
        "Add new section button not visible"

    print("Add new section button visible")

    # ==================================
    # VERIFY UPLOAD DATA FIELDS BUTTON
    # ==================================
    assert page.get_by_text(
        "Upload data fields",
        exact=False
    ).is_visible(), \
        "Upload data fields button not visible"

    print("Upload data fields button visible")

    print(
        "PASS : Data Fields page displayed "
        "all sections and fields correctly"
    )