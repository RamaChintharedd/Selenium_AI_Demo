import os


class Config:
    """Central configuration. Use environment variables to override for CI."""

    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() in ("true", "1", "yes")


__all__ = ["Config"]
