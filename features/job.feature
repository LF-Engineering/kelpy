Feature: Manage Jobs

  Scenario: Try retrieve a Job that does not exist
    Given a Job called sleepy-bohr does not exist
      When the user attempts to retrieve the Job sleepy-bohr
        Then None is returned instead of the Job


  Scenario: Create a Job
    Given a Job called strange-bhaskara does not exist
      When the Job called strange-bhaskara is created
        Then a valid Job called strange-bhaskara can be found


  Scenario: Retrieve a Job that exists
    Given the Job called lucid-lovelace exists
      When the user attempts to retrieve the Job lucid-lovelace
        Then Results for the Job lucid-lovelace are returned
