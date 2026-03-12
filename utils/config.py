import os


class Config:
    """Configuration holder. Add environment-driven overrides as needed."""
    BASE_URL = os.getenv("BASE_URL", "https://demowebshop.tricentis.com")
    DEFAULT_BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
