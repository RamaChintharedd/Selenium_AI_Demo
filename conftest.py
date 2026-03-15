import os
import pytest
from src.utils.driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption('--base-url', action='store', default=os.getenv('BASE_URL', 'https://www.amazon.com'))


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--base-url')


@pytest.fixture(scope='function')
def driver(request):
    """Create a WebDriver instance for each test and quit after test completes."""
    drv = create_driver()
    yield drv
    try:
        drv.quit()
    except Exception:
        pass
