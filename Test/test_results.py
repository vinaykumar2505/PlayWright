import pytest
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from pages.home import Hompage
from pages.result import ResultPage



@pytest.mark.test3

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




@pytest.mark.test3
def test_validate_product_count_on_results(page: Page, launchurl, homepageobj, resultpageobj):
    """
    Test Case 1: Validate that search results load with visible products.
    Steps:
        1. Search for "iphone"
        2. Get product count
        3. Assert count > 0
    """
    homepageobj.enterTextSearch("iphone")
    homepageobj.clickSearch()
    page.wait_for_timeout(2000)

    product_count = resultpageobj.get_product_count()
    assert product_count > 0, f"Expected products on results page, got {product_count}"


@pytest.mark.test3
def test_apply_price_filter_on_results(page: Page, launchurl, homepageobj, resultpageobj):
    """
    Test Case 2: Validate price filter reduces product count.
    Steps:
        1. Search for "iphone"
        2. Get initial product count
        3. Apply price filter (min: 30000, max: 50000)
        4. Get filtered product count
        5. Assert filtered count <= initial count
    """
    homepageobj.enterTextSearch("iphone")
    homepageobj.clickSearch()
    page.wait_for_timeout(2000)

    initial_count = resultpageobj.get_product_count()
    
    resultpageobj.apply_price_filter("30000", "50000")
    filtered_count = resultpageobj.get_filtered_product_count()
    
    assert filtered_count <= initial_count, \
        f"Filtered count ({filtered_count}) should be <= initial count ({initial_count})"


@pytest.mark.test3
def test_validate_product_details_visibility(page: Page, launchurl, homepageobj, resultpageobj):
    """
    Test Case 3: Validate product details (title, price, rating) are visible.
    Steps:
        1. Search for "iphone"
        2. Get first product title, price, and rating
        3. Assert all are non-empty strings
    """
    homepageobj.enterTextSearch("iphone")
    homepageobj.clickSearch()
    page.wait_for_timeout(2000)

    title = resultpageobj.get_first_product_title()
    price = resultpageobj.get_first_product_price()
    rating = resultpageobj.get_first_product_rating()

    assert title and len(title) > 0, "Product title should not be empty"
    assert price and len(price) > 0, "Product price should not be empty"
    assert rating and len(rating) > 0, "Product rating should not be empty"
