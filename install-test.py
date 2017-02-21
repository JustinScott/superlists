import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    #setup
    _browser = webdriver.Firefox()
    yield _browser
    #teardown
    _browser.quit()


def test_can_start_a_list_and_retrieve_it_later(browser):
    browser.get('http://localhost:8000')
    assert "To-Do" in browser.title
    pytest.fail("Finish writing the test.")
