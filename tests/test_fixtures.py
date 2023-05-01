"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture()
def open_browser_with_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')


@pytest.fixture()
def open_browser_with_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.open('https://github.com/')


def test_github_desktop(open_browser_with_desktop):
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_mobile(open_browser_with_mobile):
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))
