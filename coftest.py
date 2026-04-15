import pytest
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser_page():
    login_page = LoginPage("https://cs.sberbank.ru/")
    page = login_page.start_browser()
    login_page.goto()
    yield page
    login_page.close()