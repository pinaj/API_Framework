# Created by Pinaj at 07-03-2024
Feature: Verify if the book is added and deleted successfully using API
  @smoke
  Scenario: Verify the add book functionality
    Given the books details which neeed to be added
    When when the AddBook post api is being executed
    Then the book is successfully added

  @regression
    Scenario Outline: Verify the add book functionality
    Given the books details with <isbn> and <aisle>
    When when the AddBook post api is being executed
    Then the book is successfully added
      Examples:
        |isbn  |aisle |
        |book  |123   |
        |BOOK2 |122   |

