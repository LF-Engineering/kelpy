Feature: Interact with the Namespace API

  Scenario: Create a namespace and check it exists
    Given that a namespace called washington does not exist
      When the user creates a namespace called washington
        Then the washington namespace is returned

  Scenario: Retrieve a namespace that exists
    Given a namespace called bread exists
      When the user retrieves the namespace
        Then the namespace is returned

  Scenario: Retrieves a missing namespace
    Given a namespace called rain does not exist
      When the user attempts to retreive the namespace
        Then None is returned
