import pytest
from playwright.sync_api import sync_playwright
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
import os


@pytest.fixture
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=[
                "--start-maximized",
                "--force-device-scale-factor=1"
            ]
        )

        context = browser.new_context(
            no_viewport=True
        )

        page = context.new_page()

        yield page

        # Screenshot on failure
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                f"screenshots/{request.node.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"\nScreenshot saved: {screenshot_path}")

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def login(page):

    page.goto(LOGIN_URL)

    # Wait for page load
    page.wait_for_timeout(2000)

    # Login
    page.fill("input[type='text']", USERNAME)
    page.fill("input[type='password']", PASSWORD)

    page.click("button")

    page.wait_for_timeout(3000)

    return page

#def pytest_configure(config):

    config._metadata["Project Name"] = "CQFK Invoice UI"

    config._metadata["Environment"] = "QA"

    config._metadata["Browser"] = "Chromium"

    config._metadata["Automation"] = "Playwright + Pytest"