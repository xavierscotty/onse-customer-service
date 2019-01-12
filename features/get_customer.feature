Feature: Get the customer based on id
  As a service I want to get the customer details so that I can check whether they exist.

  Scenario: Fetching existing customer
    Given customer "Joe Bloggs" with ID "12345" exists
    When I fetch customer "12345"
    Then I should see customer "Joe Bloggs"

  Scenario: Fetching customer which doesn't exist
    Given there is no customer with ID "99999"
    When I fetch customer "99999"
    Then I should get a not found response
