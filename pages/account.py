from playwright.sync_api import Page

class AccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_and_lists = page.get_by_text("Account & Lists")
        self.returns_and_orders = page.get_by_role("link", name="Returns & Orders")

    def click_account_and_lists(self):
        """Click the 'Account & Lists' header element."""
        self.account_and_lists.click()

    def click_returns_and_orders(self):
        """Click the 'Returns & Orders' link."""
        self.returns_and_orders.click()

    def get_account_display_name(self) -> str:
        """Extract the display name from the 'Hello, <Name>' header (best-effort)."""
        txt = self.account_and_lists.inner_text()
        lines = txt.splitlines()
        if len(lines) >= 1:
            return lines[0].replace("Hello,", "").strip()
        return txt
