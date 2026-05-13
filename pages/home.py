from playwright.sync_api import expect


class Hompage:
    def __init__(self, page):
        self.searchBar = page.locator("#twotabsearchtextbox")
        self.carticon=page.locator("#nav-cart-count")
        self.accountsandlist = page.get_by_text("Account & Lists")
        self.searchurl = page.get_by_placeholder("Search Amazon.in")
        self.enterSearch = page.locator("#twotabsearchtextbox")
        self.clickSearchBtn = page.locator("#nav-search-submit-button")

    def searchbarVisibility(self):
        self.searchBar.wait_for(state="visible")
    def enterTextSearch(self,product):
        self.enterSearch.wait_for(state="visible")
        self.enterSearch.fill(product)
    def clickOnaccountsandlist(self):
        self.accountsandlist.click()
    def cartIconVisibility(self):
        self.carticon.wait_for(state="visible")
    def clickSearch(self):
        self.clickSearchBtn.click()
    def accountandlistVisibility(self):
        expect(self.accountsandlist).to_be_visible()
    def searchurly(self):
        expect(self.searchurl).to_be_visible()

