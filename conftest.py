import allure
import pytest

from pages.home import Hompage
from pages.login import LoginPage
from pages.result import ResultPage


@pytest.fixture
def homepageobj(page):
    homepageobj_fixture = Hompage(page)
    return homepageobj_fixture
@pytest.fixture
def loginpageobj(page):
    loginpage_fixture = LoginPage(page)
    return loginpage_fixture

@pytest.fixture
def resultpageobj(page):
    resultpageobj_fixture = ResultPage(page)
    return resultpageobj_fixture
@pytest.fixture(autouse=True)
def launchurl(page):
    page.goto("https://www.amazon.in/")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page =item.funcargs.get("page",None)
        if page:
            step = report.when
            screenshot = page.screenshot()
            allure.attach(screenshot,name=f"failure screenshot ({step})",attachment_type=allure.attachment_type.PNG)