import pytest
import os
from utils.driver_factory import create_chrome_driver


@pytest.fixture(scope="session")
def driver():
    """Session-scoped WebDriver. Tear down at session end."""
    headless = os.environ.get("HEADLESS", "false").lower() == "true"
    drv = create_chrome_driver(headless=headless)
    yield drv
    try:
        drv.quit()
    except Exception:
        pass


@pytest.fixture
def base_url():
    return os.environ.get("BASE_URL", "https://demowebshop.tricentis.com")
