import pytest

def test_login_success(browser_page):
    assert "Платформа СберБанка" in browser_page.content()