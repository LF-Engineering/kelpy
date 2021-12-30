Feature: Manage CronJobs

  Scenario: Try retrieve a CronJob that does not exist
    Given a CronJob called hello does not exist
      When the user attempts to retrieve the CronJob hello
        Then None is returned instead of the CronJob


  Scenario: Create a CronJob
    Given a CronJob called salamander does not exist
      When the CronJob called salamander is created
        Then a valid CronJob called salamander can be found


  Scenario: Retrieve a CronJob that exists
    Given the CronJob called hello exists
      When the user attempts to retrieve the CronJob hello
        Then Results for the CronJob hello are returned
