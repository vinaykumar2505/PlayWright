import pytest

from pages.home import Hompage
from pages.result import ResultPage


@pytest.fixture
def homepageobj(page):
    homepageobj_fixture = Hompage(page)
    return homepageobj_fixture

@pytest.fixture
def resultpageobj(page):
    resultpageobj_fixture = ResultPage(page)
    return resultpageobj_fixture
@pytest.fixture(autouse=True)
def launchurl(page):
    page.goto("https://www.amazon.in/")