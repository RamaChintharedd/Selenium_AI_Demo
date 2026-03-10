from typing import Final

# Centralized configuration values used across the test suite
BASE_URL: Final[str] = "https://example.com"
IMPLICIT_WAIT: Final[int] = 5
PAGE_LOAD_TIMEOUT: Final[int] = 30

# Browser to use for local runs: 'chrome' or 'firefox'
BROWSER: Final[str] = "chrome"
