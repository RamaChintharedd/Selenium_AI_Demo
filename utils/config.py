import os

# Centralized configuration values
BASE_URL = os.getenv("BASE_URL", "https://demowebshop.tricentis.com")
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))

# Test credentials (for demonstration). In real usage, secure these values in a vault or CI secrets.
VALID_EMAIL = os.getenv("DEMO_VALID_EMAIL", "user@example.com")
VALID_PASSWORD = os.getenv("DEMO_VALID_PASSWORD", "Password123")
INVALID_EMAIL = "invalid-email"
INCORRECT_PASSWORD = "wrongPassword"
