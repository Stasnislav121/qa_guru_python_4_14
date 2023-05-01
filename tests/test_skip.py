"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have, browser


@pytest.fixture(params=['desktop', 'mobile'])
def open_browser(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
    yield request.param


def test_github_desktop(open_browser):
    if open_browser != 'desktop':
        pytest.skip("Тест только для десктопной версии")
    else:
        browser.open('https://github.com/')
        browser.element('.HeaderMenu-link--sign-in').click()
        assert browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_mobile(open_browser):
    if open_browser != 'mobile':
        pytest.skip("Тест только для мобильной версии")
    else:
        browser.open('https://github.com/')
        browser.element('.Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
        assert browser.element('#login').should(have.text('Sign in to GitHub'))
