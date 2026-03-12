import pytest
from utils.driver_factory import create_driver
from utils.config import Config


@pytest.fixture(scope="function")
def driver(request):
    """Creates a WebDriver instance for each test and quits after the test finishes.
    Using function scope keeps tests isolated.
    """
    drv = create_driver(browser=Config.BROWSER, headless=Config.HEADLESS)
    drv.maximize_window()
    yield drv
    try:
        drv.quit()
    except Exception:
        pass
