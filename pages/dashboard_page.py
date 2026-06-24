from locators.dashboard_locator import DashboardLocators


class DashboardPage:

    def __init__(self, page):
        self.page = page

    # ---------------------------
    # BASIC VISIBILITY CHECKS
    # ---------------------------

    def is_home_visible(self):
        return self.page.locator(DashboardLocators.HOME).is_visible()

    def is_model_name_visible(self):
        return self.page.locator(DashboardLocators.MODEL_NAME).is_visible()

    def is_loaded(self):
        return self.is_home_visible()

    # ---------------------------
    # TABLE HEADERS
    # ---------------------------

    def get_header_text_list(self):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("th", timeout=20000)

        headers = self.page.locator("table th")
        text_list = headers.all_inner_texts()

        return [t.strip() for t in text_list if t.strip()]

    # ---------------------------
    # MODEL ACTIONS
    # ---------------------------

    def click_model_name(self):

        model = self.page.locator(
            DashboardLocators.MODEL_NAME_LINK
        )

        model.wait_for(state="visible")

        model.click()

        self.page.wait_for_load_state("networkidle")

    def click_model_id_header(self):
        self.page.locator(DashboardLocators.MODEL_ID_HEADER).click()

    def click_date_created_header(self):
        self.page.locator(DashboardLocators.DATE_CREATED_HEADER).click()

    # ---------------------------
    # ACTION MENU
    # ---------------------------

    def click_action_menu(self):
        self.page.locator(DashboardLocators.ACTION_MENU).first.click()

    def is_refresh_visible(self):
        return self.page.locator("a.dropdown-item").first.is_visible()

    def click_refresh(self):
        refresh_btn = self.page.locator("a.dropdown-item").first
        refresh_btn.wait_for(state="visible")
        refresh_btn.click()

    # ---------------------------
    # MODEL SPECIFIC ACTIONS
    # ---------------------------

    def click_taas_model(self):
        self.page.locator(DashboardLocators.TAAS_MODEL).click()

    def click_taas(self):

        taas = self.page.locator(
           "text=TAAS"
        ).first

        taas.wait_for(state="visible")

        taas.click()

        self.page.wait_for_load_state("networkidle")


    def click_taas_luy(self):

        taas_luy = self.page.locator(
            "text=TAAS (LUY)"
        )

        taas_luy.wait_for(state="visible")

        taas_luy.click()

        self.page.wait_for_load_state("networkidle")

    # ---------------------------
    # CONFIGURE MODEL
    # ---------------------------

    def is_configure_model_visible(self):
        return self.page.locator(DashboardLocators.CONFIGURE_MODEL).first.is_visible()

    def click_configure_model(self):
        self.page.locator(DashboardLocators.CONFIGURE_MODEL).first.click()

    # ---------------------------
    # TRAINING
    # ---------------------------

    def is_training_visible(self):
        return self.page.locator("p.card-title", has_text="Training").is_visible()

    # ---------------------------
    # PROCESSING DASHBOARD
    # ---------------------------

    def is_processing_dashboard_visible(self):
        return self.page.locator(DashboardLocators.PROCESSING_DASHBOARD).first.is_visible()

    def is_processing_dashboard_clickable(self):
        return self.page.locator(DashboardLocators.PROCESSING_DASHBOARD).first.is_enabled()

    def click_processing_dashboard(self):

        processing = self.page.locator(
            DashboardLocators.PROCESSING_DASHBOARD
        ).first

        processing.wait_for(state="visible")

        processing.click()

        self.page.wait_for_load_state("networkidle")

    # ---------------------------
    # DOCUMENT ANALYTICS
    # ---------------------------

    def is_document_analytics_visible(self):
        locator = self.page.locator(DashboardLocators.DOCUMENT_ANALYTICS)
        locator.first.wait_for(state="visible", timeout=10000)
        return locator.first.is_visible()
    
    def open_review_status_dropdown(self):
        self.page.locator("#review-status-select").click()

    def select_review_status(self, status):

        self.page.wait_for_selector("li[role='option']", timeout=5000)

        self.page.locator(
            f"li[role='option']:has-text('{status}')"
        ).first.click()
    def get_all_review_status_values(self):

        rows = self.page.locator("table tbody tr")

        count = rows.count()
        status_list = []

        for i in range(count):

        # IMPORTANT: adjust index if needed
           status = rows.nth(i).locator("td").nth(4).inner_text()

           status_list.append(status.strip().lower())

        return status_list
    
    def get_processed_count(self):
        return int(
            self.page.locator("p:has-text('Processed')")
            .locator("xpath=following-sibling::p")
            .inner_text()
            .strip()
        )
    def get_unprocessed_count(self):
        return int(
            self.page.locator("p:has-text('Unprocessed')")
            .first
            .locator("xpath=following-sibling::p")
            .inner_text()
            .strip()
        )
    def get_review_status_count(self, status):

        review_card = self.page.locator(
            f"p:has-text('{status}')"
        ).first

        count = review_card.locator(
            "xpath=following-sibling::p"
        ).inner_text()

        return int(count.strip())
     # ---------------------------
    # Processing Status dropdown
    # ---------------------------
    def open_doc_status_dropdown(self):
        self.page.locator("#doc-status-select").click()


    def select_doc_status(self, status):
        self.page.locator(
            f"li[role='option'][data-value='{status.lower()}']"
        ).click()


    def get_total_documents_count(self):

        value = self.page.locator(
            "//div[contains(text(),'Total Documents')]/following-sibling::div[1]"
        )

        print("Total Documents =", value.inner_text())

        return int(value.inner_text().strip())
    
    # Validation Status Dropdown
    def open_color_status_dropdown(self):
        self.page.locator("#color-status-select").click()

    def select_color_status(self, color):
        self.page.locator(
            f"li[role='option'][data-value='{color.lower()}']"
        ).click()
    # ---------------------------
    # Table Header
    # ---------------------------
    
    def get_table_headers(self):

        headers = self.page.locator("table thead th")

        return [
            headers.nth(i).inner_text().strip()
            for i in range(headers.count())
        ]
     # ---------------------------
    # search_functionality
    # ---------------------------
    def search_document(self, value):

        search_box = self.page.locator(
            "input[placeholder='Type to search...']"
        )

        search_box.wait_for(state="visible")

        search_box.fill("")

        search_box.fill(value)

        self.page.wait_for_load_state("networkidle")

    def get_first_doc_id(self):
        return (
            self.page.locator("table tbody tr")
            .first
            .locator("td")
            .nth(1)
            .inner_text()
            .strip()
        )


    def get_first_document_name(self):
        return (
            self.page.locator("table tbody tr")
            .first
            .locator("td")
            .nth(2)
            .inner_text()
            .strip()
        )
    # ---------------------------
# COMMON WAITS
# ---------------------------

    def wait_for_table(self):

        self.page.locator(
            "table tbody tr"
        ).first.wait_for(
        state="visible",
        timeout=30000
        )


    def wait_for_loader_to_disappear(self):

        self.page.wait_for_load_state(
            "networkidle"
        )


    def wait_for_search_results(self):

        self.page.locator(
            "table tbody tr"
        ).first.wait_for(
            state="visible",
            timeout=30000
        )



