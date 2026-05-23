import pytest
from playwright.sync_api import Page

from utils.jsonhandlingfile import jsonFile
filepath = "Test_Data/credential.json"
@pytest.mark.test4
def test_Cart(page:Page, launchurl, loginpageobj,homepageobj, resultpageobj):

    homepageobj.clickOnaccountsandlist()
    credentials = jsonFile(filepath)
    loginpageobj.emailTextbox(credentials["positiveCredentials"]["username"])
    loginpageobj.continueButtnclick()
    loginpageobj.paswdTextbox(credentials["positiveCredentials"]["password"])
    loginpageobj.pswdSignInButton()
    resultpageobj.cartnumber()
    homepageobj.enterTextSearch("iphone")
    homepageobj.clickSearch()
