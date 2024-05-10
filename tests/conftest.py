import pytest
from selenium import webdriver as wd

from urls import main_url


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", type=str)


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = None
    if browser_name == "firefox":
        options = wd.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = wd.Firefox(options=options)
    elif browser_name == "chrome":
        options = wd.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = wd.Chrome(options=options)

    driver.get(main_url)
    yield driver
    driver.quit()
