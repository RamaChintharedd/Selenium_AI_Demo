import os


class Config:
    """Singleton configuration provider.

    Reads configuration from environment variables with sensible defaults.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        self.BASE_URL = os.getenv("BASE_URL", "https://demowebshop.tricentis.com")
        self.BROWSER = os.getenv("BROWSER", "chrome").lower()
        # Timeouts
        self.DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))


config = Config()
