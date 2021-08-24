Feature: Manage deployments

  Scenario: Try retrieve a deployment that does not exist
    Given A deployment called fog does not exist
      When The user attempts to retrieve the deployment fog
        Then returns None
	

  Scenario: Create a deployment and wait for it to become ready
    Given A deployment called whilrwind does not exist
      When The deployment called whilrwind is created
        Then a valid deployment called whilrwind can be found

  Scenario: Retrieve a deployment that exists
    Given The deployment called fire exists
      When The user attempts to retrieve the deployment fire
        Then Results for the deployment fire are returned
