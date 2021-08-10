Feature: Interact with the Namespace API and Objects

  Scenario: Create a namespace and check it exists
    When the create function is invoked
      Then a new namespace is created

  Scenario: Retrieves a missing namespace
    When a user tries to retrieve a namespace that doesn't exist None is returned.
