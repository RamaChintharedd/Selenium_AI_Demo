import os


class Config:
    """Configuration holder. Central place to manage environment variables and defaults."""

    BASE_URL = os.getenv("BASE_URL", "https://demowebshop.tricentis.com")
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # Test credentials - in real tests, use a secure secret manager or test fixture setup
    VALID_EMAIL = os.getenv("TEST_VALID_EMAIL", "user@example.com")
    VALID_PASSWORD = os.getenv("TEST_VALID_PASSWORD", "P@ssw0rd")
