Feature: Login
  Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user enters a valid username and password
    And clicks the login button
    Then the user is redirected to the dashboard
    And sees a welcome message