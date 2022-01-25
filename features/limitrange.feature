Feature: Test limitrange


       Scenario: Try retrieve a limitrange that does not exist
            Given a limitrange called test does not exist
              When the user attempts to retrieve the limitrange test
                Then None is returned instead of the limitrange

       Scenario: Create a limitrange
            Given a limitrange called test1 does not exist
              When the limitrange called test1 is created
                Then a valid limitrange called test1 can be found

       Scenario: Retrieve a limitrange that exists
            Given the limitrange called test2 exists
              When the user attempts to retrieve the limitrange test2
                Then Results for the limitrange test2 are returned
