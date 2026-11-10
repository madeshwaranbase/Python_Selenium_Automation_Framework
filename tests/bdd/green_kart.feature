Feature: GreenKart product search

  Scenario: Search for a product
    Given the GreenKart home page is open
    When the shopper searches for "cucumber"
    Then matching products should be displayed
