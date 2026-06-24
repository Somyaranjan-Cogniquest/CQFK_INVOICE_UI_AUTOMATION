from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD


import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_55_search_whitespace_and_partial_match(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # NAVIGATE TO PROCESSING DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # ==========================
    # SEARCH DOC ID WITH SPACES
    # ==========================
    search_box = page.locator("input.searchbar")

    search_box.fill(" 71460 ")

    page.wait_for_timeout(3000)

    rows_after_search = page.locator("table tbody tr").count()

    print("Rows after whitespace search:", rows_after_search)

    assert rows_after_search > 0, \
        "Search with leading/trailing spaces returned no results"

    # ==========================
    # CLEAR SEARCH
    # ==========================
    search_box.fill("")

    page.wait_for_timeout(3000)

    # ==========================
    # GET DOCUMENT NAME
    # ==========================
    documents = page.locator("div[docid]")

    assert documents.count() > 0, \
        "No documents found"

    full_doc_name = documents.first.text_content().strip()

    print("Full Document:", full_doc_name)

    # Example:
    # SHRINRG2533b8047_IRN_SHR61AC04205_PO.pdf
    partial_name = full_doc_name[:8]

    print("Partial Search:", partial_name)

    # ==========================
    # PARTIAL SEARCH
    # ==========================
    search_box.fill(partial_name)

    page.wait_for_timeout(3000)

    partial_rows = page.locator("table tbody tr").count()

    print("Rows after partial search:", partial_rows)

    assert partial_rows > 0, \
        "Partial search returned no results"

    # ==========================
    # VERIFY MATCHING RECORD
    # ==========================
    matching_docs = page.locator(f"text={partial_name}")

    assert matching_docs.count() > 0, \
        "Matching document not displayed"

    print("TC_55 PASSED")