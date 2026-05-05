import pytest

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="function")
def setup(page):
    page.goto(BASE_URL)
    yield page
    page.close()