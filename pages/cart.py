from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_header_link = page.get_by_role("link", name="items in cart")
        self.cart_items = page.locator("div.sc-list-item")  # may need tuning depending on Amazon layout
        self.cart_count = page.locator("#nav-cart-count")

    def view_cart(self):
        """Click the header 'items in cart' link."""
        self.cart_header_link.click()

    def get_cart_item_count(self) -> int:
        """Return the header cart count as an int (parsing will raise if invalid)."""
        text = self.cart_count.inner_text()
        return int(text)

    def get_number_of_cart_rows(self) -> int:
        """Return the number of cart item rows currently rendered."""
        return self.cart_items.count()

    def open_product_from_cart_by_title(self, title: str):
        """Click a product link in the cart by exact visible title."""
        self.page.get_by_role("link", name=title, exact=True).click()
