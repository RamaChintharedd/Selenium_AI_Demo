import json


def sample_payload_missing_user_stories() -> str:
    """Return a JSON string that does not include user_stories."""
    return json.dumps({
        "request_id": "req-123",
        "intent": "generate_tests"
    }, indent=2)


def sample_payload_empty_user_stories() -> str:
    """Return a JSON string with an empty user_stories array."""
    return json.dumps({
        "request_id": "req-124",
        "user_stories": []
    }, indent=2)


def sample_payload_with_user_stories() -> str:
    """Return a JSON string with a non-empty user_stories array."""
    return json.dumps({
        "request_id": "req-125",
        "user_stories": [
            {"id": "US1", "title": "Login", "description": "User can log in."},
            {"id": "US2", "title": "Logout", "description": "User can log out."}
        ]
    }, indent=2)
