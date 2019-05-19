# Created by JARV at 5/18/19
Feature: CarnivalTest
  As a job candidate
  I want to resolve automate stories 1 and 2
  So I can desmostrate my skills.

  Scenario: Search cruise from home page
    Given I access Carnival Home Page
    When I click on sail to filter
    And I select sail to "The Bahamas"
    Then I should see the results as "grid"
