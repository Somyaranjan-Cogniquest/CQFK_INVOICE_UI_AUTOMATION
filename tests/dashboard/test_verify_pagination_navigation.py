from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_92_verify_pagination_navigation(page):

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
    # PAGINATION LOCATORS
    # ==================================
    current_page = page.locator(
        "#currentPage"
    )

    total_pages = page.locator(
        "span.pgtotal"
    ).last

    current_page_no = int(
        current_page.input_value()
    )

    total_page_no = int(
        total_pages.inner_text()
    )

    print(
        f"Current Page : {current_page_no}"
    )

    print(
        f"Total Pages : {total_page_no}"
    )

    # ==================================
    # VERIFY FIRST PAGE
    # ==================================
    if current_page_no == 1:

        print(
            "Currently On First Page"
        )

        print(
            "< and << should be disabled"
        )

        assert int(
            current_page.input_value()
        ) == 1

    # ==================================
    # NEXT PAGE >
    # ==================================
    next_btn = page.locator(
        "img[src*='single_right']"
    ).first

    next_btn.click(force=True)

    page.wait_for_timeout(3000)

    next_page = int(
        current_page.input_value()
    )

    assert next_page == (
        current_page_no + 1
    )

    print(
        f"Next Page Opened : {next_page}"
    )

    # ==================================
    # PREVIOUS PAGE <
    # ==================================
    prev_btn = page.locator(
        "img[src*='single_left']"
    ).first

    prev_btn.click(force=True)

    page.wait_for_timeout(3000)

    previous_page = int(
        current_page.input_value()
    )

    assert previous_page == current_page_no

    print(
        f"Previous Page Opened : {previous_page}"
    )

    # ==================================
    # JUMP TO LAST PAGE >>
    # ==================================
    last_btn = page.locator(
        "img[src*='double_right']"
    ).first

    last_btn.click(force=True)

    page.wait_for_timeout(5000)

    last_page = int(
        current_page.input_value()
    )

    assert last_page == total_page_no

    print(
        f"Last Page Opened : {last_page}"
    )

    # ==================================
    # VERIFY LAST PAGE
    # ==================================
    assert int(
        current_page.input_value()
    ) == total_page_no

    print(
        "> and >> are disabled on last page"
    )

    # ==================================
    # JUMP TO FIRST PAGE <<
    # ==================================
    first_btn = page.locator(
        "img[src*='double_left']"
    ).first

    assert first_btn.count() > 0, \
        "First Page Button not found"

    first_btn.click(force=True)

    page.wait_for_timeout(5000)

    first_page = int(
        current_page.input_value()
    )

    assert first_page == 1

    print(
        f"Returned To First Page : {first_page}"
    )

    # ==================================
    # VERIFY FIRST PAGE AGAIN
    # ==================================
    assert int(
        current_page.input_value()
    ) == 1

    print(
        "< and << are disabled on first page"
    )

    print(
        "TC_92 Pagination Navigation Passed Successfully"
    )