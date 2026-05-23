import pytest
from playwright.sync_api import sync_playwright, expect

from pages.home import Hompage


@pytest.mark.test3
def test_homePageUIValidation(page):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
        page.goto("https://www.amazon.in/")
        homePageobj=Hompage(page)
        homePageobj.searchbarVisibility()
        homePageobj.searchurly()
        homePageobj.accountandlistVisibility()
        print("Success")
@pytest.mark.test3
def test_validateCartIcon(page):
    page.goto("https://www.amazon.in/")
    homePageobj = Hompage(page)
    homePageobj.cartIconVisibility()
    homePageobj.enterTextSearch("iphone")
    homePageobj.clickSearch()




