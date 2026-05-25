from playwright.sync_api import Page


class OrdersPage:
    def __init__(self, page: Page):
        self.page = page

        # Page header and navigation
        self.page_title = page.locator("h1")
        self.orders_filter_dropdown = page.locator("select#time-filter")

        # Order search
        self.search_orders_input = page.locator("input[type='text'][placeholder*='Search']")
        self.search_orders_button = page.locator("input[type='submit']")

        # Order cards/items
        self.order_cards = page.locator("div.order")

    def navigate_to_orders(self):
        """Navigate to Your Orders page."""
        self.page.goto("https://www.amazon.in/your-orders/orders?ref_=nav_orders_first")
        self.page.wait_for_timeout(3000)

    def get_page_title(self) -> str:
        """Returns the page title text."""
        return self.page_title.inner_text()

    def is_orders_page_loaded(self) -> bool:
        """Check if the orders page is loaded by verifying URL."""
        return 'order' in self.page.url.lower()

    def get_order_count(self) -> int:
        """Returns the number of order cards visible on the page."""
        return self.order_cards.count()

    def search_order(self, search_term: str):
        """Search for orders using the search box."""
        self.search_orders_input.fill(search_term)
        self.search_orders_button.click()
        self.page.wait_for_timeout(2000)

    def is_search_box_visible(self) -> bool:
        """Check if the order search box is visible."""
        return self.search_orders_input.is_visible()
