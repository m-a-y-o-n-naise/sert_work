import pytest

def test_login_success(browser_page):
    assert "Платформа" in browser_page.content()