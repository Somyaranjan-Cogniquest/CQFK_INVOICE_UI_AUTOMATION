from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_CM_003_verify_add_new_section_button(page):

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
    add_section_btn = page.get_by_text(
        "Add new section",
        exact=False
    )

    assert add_section_btn.is_visible(), \
        "Add new section button not visible"

    add_section_btn.click()

    page.wait_for_timeout(3000)

    print("Clicked Add New Section button")

    # ==================================
    # VERIFY PANEL OPENED
    # ==================================
    panel_opened = False

    possible_locators = [
        page.get_by_text(
            "Add New Section",
            exact=False
        ),
        page.locator(
            "input[placeholder*='Section']"
        ),
        page.locator(
            "input[name='sectionName']"
        ),
        page.locator(
            "div[role='dialog']"
        )
    ]

    for locator in possible_locators:
        try:
            if locator.first.is_visible():
                panel_opened = True
                break
        except:
            pass

    assert panel_opened, \
        "Add New Section panel did not open"

    print(
        "PASS : Add New Section panel "
        "opened successfully"
    )