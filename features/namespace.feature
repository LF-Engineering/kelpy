Feature: Interact with the Namespace API

  Scenario: Try retrieve a namespace that does not exist
    Given a namespace called rain does not exist
      When the user attempts to retrieve the namespace rain
        Then None is returned for the namespace

  Scenario: Create a namespace and check it exists
    Given a namespace called washington does not exist
      When a namespace called washington is created
        Then results containing the washington namespace are returned

  Scenario: Retrieve a namespace that exists
    Given a namespace called bread exists
      When the user retrieves the namespace bread
        Then results for the namespace bread  are returned
