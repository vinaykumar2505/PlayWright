from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.continueButtn = page.locator('//input[@class="a-button-input"]')
        self.emailbox =page.get_by_role("textbox", name="Enter mobile number or email")
        self.passwordbox =page.get_by_role("textbox", name="Password")
        self.pswdcontinueButton = page.get_by_role("button", name="Sign in", exact=True)


    def emailTextbox(self, emaild):
        self.emailbox.fill(emaild)
    def continueButtnclick(self):
        self.continueButtn.click()
    def paswdTextbox(self, passwrd):
        self.passwordbox.fill(passwrd)
    def pswdSignInButton(self):
        self.pswdcontinueButton.click()