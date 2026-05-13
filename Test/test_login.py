import json
import re
from utils.jsonhandlingfile import jsonFile
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
filepath = "Test_Data/credential.json"
@pytest.mark.test3
def test_loginPage(page, homepageobj, loginpageobj):
    page.goto("https://www.amazon.in/")
    homepageobj.clickOnaccountsandlist()
   # page.get_by_role("textbox", name="Enter mobile number or email").click()

    # reading the json file
    #with open(filepath) as json_file:
        #credentials = json.load(json_file)
    credentials =jsonFile(filepath)
    loginpageobj.emailTextbox(credentials["positiveCredentials"]["username"])
    loginpageobj.continueButtnclick()
    #page.get_by_role("textbox", name="Enter mobile number or email").fill("9966159034")
   # page.get_by_role("button", name="Continue").click()
    loginpageobj.paswdTextbox(credentials["positiveCredentials"]["password"])
    #page.get_by_role("textbox", name="Password").fill("Laksh1990@@@@@")
    #page.get_by_role("button", name="Sign in", exact=True).click()
    loginpageobj.pswdSignInButton()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
