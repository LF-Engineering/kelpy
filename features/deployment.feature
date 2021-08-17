Feature: Manage deployments

  Scenario: Create a deployment and wait for it to become ready
    Given A deployment called whilrwind does not exist
      When the deployment called whilrwind is created
      #And the create operation waits for it to become ready
      Then a valid deployment called whilrwind can be found
