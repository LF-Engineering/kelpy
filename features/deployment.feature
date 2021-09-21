Feature: Manage deployments

  Scenario: Try retrieve a deployment that does not exist
    Given a deployment called fog does not exist
      When the user attempts to retrieve the deployment fog
        Then None is returned instead of the deployment


  Scenario: Create a deployment and wait for it to become ready
    Given a deployment called whilrwind does not exist
      When the deployment called whilrwind is created
        Then a valid deployment called whilrwind can be found

  Scenario: Retrieve a deployment that exists
    Given the deployment called fire exists
      When the user attempts to retrieve the deployment fire
        Then Results for the deployment fire are returned
