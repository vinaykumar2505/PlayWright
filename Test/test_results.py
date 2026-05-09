import pytest
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from pages.home import Hompage
from pages.result import ResultPage



@pytest.mark.resutt
def test_validatingCartCount(page:Page, launchurl, homepageobj, resultpageobj):
    #page.goto("https://www.amazon.in/")
    #homepageobj= Hompage(page)
    #resultpageobj = ResultPage(page)
    homepageobj.enterTextSearch("iphone 17 pro")
    homepageobj.clickSearch()
    page.wait_for_timeout(3000)
    count_beforecart_number = resultpageobj.cartnumber()
    resultpageobj.addcart('iPhone 17e 256 GB:')
    page.wait_for_timeout(3000)
    count_aftercart_number = resultpageobj.cartnumber()
    assert int(count_aftercart_number) > int(count_beforecart_number)

def test_validatingCartCount_1(page:Page):
    page.goto("https://www.amazon.in/")
    homepageobj= Hompage(page)
    resultpageobj = ResultPage(page)
    homepageobj.enterTextSearch("iphone 17 pro")
    homepageobj.clickSearch()
    page.wait_for_timeout(3000)
    count_beforecart_number = resultpageobj.cartnumber()
    resultpageobj.addcart('iPhone 17e 256 GB:')
    page.wait_for_timeout(3000)
    count_aftercart_number = resultpageobj.cartnumber()
    assert int(count_aftercart_number) > int(count_beforecart_number)



