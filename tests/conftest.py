import pytest
from utils.driver_factory import create_driver
from utils.config import Config


@pytest.fixture(scope="function")
def driver(request):
    """Create a webdriver instance for each test and quit afterwards."""
    browser = Config.DEFAULT_BROWSER
    headless = Config.HEADLESS
    driver = create_driver(browser=browser, headless=headless)

    yield driver

    try:
        driver.quit()
    except Exception:
        pass
