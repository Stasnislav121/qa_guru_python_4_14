"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import have, browser


@pytest.fixture(params=['desktop', 'mobile'])
def open_browser(request, url='https://github.com/'):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open(url)

    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
        browser.open(url)
    yield browser


@pytest.mark.parametrize('open_browser', ['desktop'], indirect=True)
def test_github_desktop(open_browser):
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('open_browser', ['mobile'], indirect=True)
def test_github_mobile(open_browser):
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))
