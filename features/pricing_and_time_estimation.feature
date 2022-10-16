Feature: Pricing and time estimation present on the page
  As a user that wants to translate some text, I want to check the price of translation and how long would it take

  Scenario: Check for pricing and time estimation presence
    Given user is on the homepage
    When user clicks 'Wyceń i zamów tłumaczenie' button to choose the service
    And user chooses to translate from Polish to German
    And user checks box 'dodatkowa korekta native speakera'
    And user fills in 250-400 words to translate into the text field
    And e-mail field stays empty
    Then pricing and time estimation should be present