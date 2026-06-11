import pytest
from playwright.sync_api import sync_playwright
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

import os

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )

        page = context.new_page()

        yield page

        # Take screenshot if test failed
        if request.node.rep_call.failed:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                f"screenshots/{request.node.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"\nScreenshot saved: {screenshot_path}")

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def login(page):

    page.goto(LOGIN_URL)

    # wait page load
    page.wait_for_timeout(2000)

    # FIX selectors (most common safe ones)
    page.fill("input[type='text']", USERNAME)
    page.fill("input[type='password']", PASSWORD)

    page.click("button")

    page.wait_for_timeout(3000)

    return page