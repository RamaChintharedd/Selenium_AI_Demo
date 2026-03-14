from pathlib import Path

# Centralized configuration for tests and environment
BASE_URL = "https://demowebshop.tricentis.com"
# Credentials: supply real test credentials via environment variables or CI secrets
# For local runs you can override these values or extend config to read from env
REGISTERED_EMAIL = "user@example.com"
REGISTERED_PASSWORD = "<correct_password>"
CHROME_DRIVER_PATH = None  # set to path if needed, otherwise rely on chromedriver in PATH
DEFAULT_TIMEOUT = 10

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
