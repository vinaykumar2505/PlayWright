import page
from playwright.sync_api import expect, Page


class ResultPage:
    def __init__(self, page:Page):
        self.cartCount= page.locator("#nav-cart-count")
        #self.addtoCart= lambda product: page.locator(f"//span[contains(text(),'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[text()='Add to cart']")
        self.addtoCart = lambda product: page.locator(
            f"//span[contains(text(),'{product}')]/ancestor::div[contains(@class,'s-widget-container')]//button[text(),'Add to cart']")

    def addcart(self, itemName):
        self.addtoCart(itemName).first.click()
    def cartnumber(self):
        return self.cartCount.inner_text()


