from playwright.sync_api import sync_playwright

class PlaywrightManager:

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

        return self.page

    def stop(self):
        self.browser.close()
        self.playwright.stop()