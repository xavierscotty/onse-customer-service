Feature: Get the customer based on id
    As a service I want to get the customer details so that I can check whether they exist.

    Scenario: Fetching example customer
        When I fetch customer 12345
        Then I should see customer "Joe Bloggs"
    