import os
import pathlib
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='session')
def app_page_path() -> str:
    """Provide the file:// absolute URL to the test HTML page."""
    # Resolve the local app/assistant.html relative to project root
    root = pathlib.Path(__file__).parent.resolve()
    local_path = root / 'app' / 'assistant.html'
    return 'file://' + str(local_path)


@pytest.fixture
def driver():
    """Create a Chrome WebDriver instance for tests. Quits after tests complete."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1200, 900)
    yield driver
    driver.quit()
