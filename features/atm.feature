Feature: ATM operations

  Scenario: Successful withdrawal
    Given I have $100 in my account
    When I withdraw $40
    Then I should have $60 left in my account

  Scenario: Successful deposit
    Given I have $100 in my account
    When I deposit $50
    Then I should have $150 in my account

  Scenario: Check balance
    Given I have $100 in my account
    When I check my balance
    Then I should see that my balance is $100