import time
import pytest

from pages.assistant_page import AssistantPage
from utils.json_utils import (
    sample_payload_missing_user_stories,
    sample_payload_empty_user_stories,
    sample_payload_with_user_stories,
)


# Per requirements: wait 2 seconds before proceeding to the next request/test
WAIT_BETWEEN_REQUESTS = 2


def test_prompt_when_user_stories_missing_or_empty(driver, app_page_path):
    """
    Scenario: Prompt user when user_stories array is missing or empty
      Given the assistant receives a request to generate test cases
      And the request payload does not contain a 'user_stories' JSON array or the 'user_stories' array is empty
      When the assistant inspects the request payload
      Then the assistant returns a clear prompt asking the user to provide the 'user_stories' JSON array in the expected format
      And the assistant waits for the user's response
    """
    page = AssistantPage(driver, app_page_path)
    page.load()

    # Case A: missing user_stories
    page.set_payload(sample_payload_missing_user_stories())
    page.click_inspect()
    time.sleep(0.5)
    resp = page.get_response_text()
    assert 'Please provide the "user_stories" JSON array' in resp
    assert page.is_prompt_visible()

    # Wait between requests as required
    time.sleep(WAIT_BETWEEN_REQUESTS)

    # Case B: empty user_stories
    page.set_payload(sample_payload_empty_user_stories())
    page.click_inspect()
    time.sleep(0.5)
    resp2 = page.get_response_text()
    assert 'Please provide the "user_stories" JSON array' in resp2
    assert page.is_prompt_visible()


def test_continue_when_user_provides_user_stories(driver, app_page_path):
    """
    Scenario: Continue when user provides user_stories
      Given the assistant has previously prompted the user for the 'user_stories' JSON array
      When the user supplies a valid, non-empty 'user_stories' JSON array
      Then the assistant proceeds to generate test cases per the specified output format
      And the assistant returns the generated test cases in the required JSON structure
    """
    page = AssistantPage(driver, app_page_path)
    page.load()

    # Simulate prior prompt by first giving an invalid payload
    page.set_payload(sample_payload_missing_user_stories())
    page.click_inspect()
    time.sleep(0.5)
    assert page.is_prompt_visible()

    # Wait between requests as required
    time.sleep(WAIT_BETWEEN_REQUESTS)

    # Now supply a valid user_stories array
    page.set_payload(sample_payload_with_user_stories())
    page.click_inspect()
    time.sleep(0.5)
    resp = page.get_response_text()

    assert 'Received 2 user_stories' in resp
    assert page.is_ok_visible()
