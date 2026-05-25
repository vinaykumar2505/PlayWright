from playwright.sync_api import Page


class ResultPage:
    def __init__(self, page: Page):
        # keep the page reference
        self.page = page
        self.cartCount = page.locator("#nav-cart-count")
        
        # Parameterized add-to-cart locator
        self.addtoCart = lambda product: page.locator(
            f"//span[contains(text(),'{product}')]/ancestor::div[contains(@class,'s-widget-container')]//button[contains(normalize-space(.),'Add to cart')]"
        )
        
        # New locators for results page testing (test cases 1-3)
        self.product_items = page.locator("div[data-component-type='s-search-result']")
        self.product_title = lambda idx: page.locator(f"div[data-component-type='s-search-result']:nth-of-type({idx}) h2 a span")
        self.product_price = lambda idx: page.locator(f"div[data-component-type='s-search-result']:nth-of-type({idx}) .a-price-whole")
        self.product_rating = lambda idx: page.locator(f"div[data-component-type='s-search-result']:nth-of-type({idx}) .a-icon-star-small span")
        
        # Price filter locators
        self.min_price_input = page.locator("input[aria-label*='Min']")
        self.max_price_input = page.locator("input[aria-label*='Max']")
        self.apply_price_filter_button = page.locator("input[aria-label*='Go']")

    def addcart(self, itemName: str):
        """Click the first Add to cart button for the given product text."""
        self.addtoCart(itemName).first.click()

    def cartnumber(self) -> str:
        """Return the cart count shown in the header as text."""
        return self.cartCount.inner_text()

    def get_product_count(self) -> int:
        """Returns the total number of product items visible on the search results page."""
        return self.product_items.count()

    def apply_price_filter(self, min_price: str, max_price: str):
        """Apply a price filter to the search results."""
        self.min_price_input.fill(min_price)
        self.max_price_input.fill(max_price)
        self.apply_price_filter_button.click()
        self.page.wait_for_timeout(2000)

    def get_filtered_product_count(self) -> int:
        """Returns the number of products after applying a filter."""
        return self.product_items.count()

    def get_first_product_title(self) -> str:
        """Returns the title of the first product in the search results."""
        return self.product_title(1).inner_text()

    def get_first_product_price(self) -> str:
        """Returns the price of the first product in the search results."""
        return self.product_price(1).inner_text()

    def get_first_product_rating(self) -> str:
        """Returns the star rating of the first product."""
        return self.product_rating(1).inner_text()
