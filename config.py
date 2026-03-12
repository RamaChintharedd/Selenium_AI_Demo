import os

# Configuration constants
BASE_URL = os.getenv('BASE_URL', 'https://demowebshop.tricentis.com')
LOGIN_URL = f"{BASE_URL}/login"

# Provide credentials via environment variables for security
REGISTERED_EMAIL = os.getenv('REGISTERED_EMAIL', 'registered_user@example.com')
REGISTERED_PASSWORD = os.getenv('REGISTERED_PASSWORD', 'replace_with_valid_password')

# Timeouts
DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '10'))
