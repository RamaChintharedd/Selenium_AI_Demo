import pytest
from utils.driver_factory import DriverFactory
from utils.config import Config
from utils.logger import get_logger


LOGGER = get_logger(__name__)


@pytest.fixture(scope="session")
def config():
    """Provide configuration to tests."""
    return Config


@pytest.fixture(scope="function")
def driver(request, config):
    """Create a WebDriver instance for each test and quit afterwards."""
    driver = DriverFactory.create_driver()
    LOGGER.info("Starting browser for test: %s", request.node.name)
    yield driver
    LOGGER.info("Quitting browser for test: %s", request.node.name)
    try:
        driver.quit()
    except Exception:
        pass
