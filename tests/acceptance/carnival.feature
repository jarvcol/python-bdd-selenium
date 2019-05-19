# Created by JARV at 5/18/19
Feature: CarnivalTest
  As a job candidate
  I want to resolve automate stories 1 and 2
  So I can desmonstrate my skills.

  Scenario: Search cruise from home page and filter by price
    Given I access Carnival Home Page
    When I click on sail to filter
    And I select sail to "The Bahamas"
    Then I should see the results as "grid"
    When I click on the pricing filter
    And I move lower pricing pointer up to "600"
    Then I should see cruise results between "600" and "800"
    When I click on reset filter button
    And I move higher pricing pointer up to "500"
    Then I should see cruise results between "100" and "500"
