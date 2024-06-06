from selene import browser, by, be, have
import pytest
import allure

def test_github_issue():

    with allure.step('open github page'):
        browser.open('https://github.com/')

    with allure.step('click on input field'):
        browser.element('[data-target="qbsearch-input.inputButton"]').click()

    with allure.step('type eroshenko am'):
        browser.element('#query-builder-test').type('eroshenkoam/allure-examples').press_enter()

    with allure.step('click issues'):
        browser.element(by.link_text('Issues')).click()

    with allure.step('check 66 issue'):
        browser.element(by.partial_link_text('asd#66')).should(be.visible)