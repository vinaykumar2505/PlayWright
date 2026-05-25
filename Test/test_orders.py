import pytest
from playwright.sync_api import Page

from pages.home import Hompage
from pages.login import LoginPage
from pages.orders import OrdersPage
from utils.jsonhandlingfile import jsonFile


filepath = "Test_Data/credential.json"


@pytest.mark.orders
def test_verify_orders_page_loads_after_login(page: Page, homepageobj, loginpageobj, orderspageobj):
    """
    Test Case 1: Verify Orders Page Loads Successfully After Login

    Steps:
        1. Navigate to Amazon homepage
        2. Click on "Account & Lists" to login
        3. Enter credentials and login
        4. Navigate to "Returns & Orders" / Your Orders page
        5. Verify the orders page is loaded
    """
    page.goto("https://www.amazon.in/")
    homepageobj.clickOnaccountsandlist()
    page.wait_for_timeout(2000)

    credentials = jsonFile(filepath)
    loginpageobj.emailTextbox(credentials["positiveCredentials"]["username"])
    loginpageobj.continueButtnclick()
    page.wait_for_timeout(2000)

    loginpageobj.paswdTextbox(credentials["positiveCredentials"]["password"])
    loginpageobj.pswdSignInButton()
    page.wait_for_timeout(3000)

    orderspageobj.navigate_to_orders()

    assert orderspageobj.is_orders_page_loaded(), "Orders page did not load successfully"
    print("✓ Orders page loaded successfully")


@pytest.mark.orders
def test_verify_orders_filter_dropdown(page: Page, homepageobj, loginpageobj, orderspageobj):
    """
    Test Case 2: Verify Orders Filter Dropdown is Visible

    Steps:
        1. Navigate to Amazon homepage
        2. Login with valid credentials
        3. Navigate to Your Orders page
        4. Verify filter dropdown is visible
    """
    page.goto("https://www.amazon.in/")
    homepageobj.clickOnaccountsandlist()
    page.wait_for_timeout(2000)

    credentials = jsonFile(filepath)
    loginpageobj.emailTextbox(credentials["positiveCredentials"]["username"])
    loginpageobj.continueButtnclick()
    page.wait_for_timeout(2000)

    loginpageobj.paswdTextbox(credentials["positiveCredentials"]["password"])
    loginpageobj.pswdSignInButton()
    page.wait_for_timeout(3000)

    orderspageobj.navigate_to_orders()

    assert orderspageobj.orders_filter_dropdown.is_visible(), "Orders filter dropdown is not visible"

    print("✓ Orders filter dropdown is visible")
