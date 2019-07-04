# Pivotal Tests

**Overview**

This project's objective is to set up some testing for the Pivotal Tracker API.

**Requirements**

This project was intended to work with python 3.6. 
This means all required libraries should be installed with "pip3 install".
A list of required libraries can be found on "requirements.txt" file.

**About the project**

On the 'core' folder we intend to put generic steps and functions that can be used on any API testing. 
We also included a generic API request class, this class can be inherited to customize request options.

**Setting Up - PIVOTAL TRACKER**

Go to "pivotal_tracker" folder inside the project directory.
There you will find a "config.dist" file (Configurations are based on json file format). 
This file contains all the configuration that will be used for the testing.
It should be filled as indicated (all examples are based on APIv5):

* "BASE_URL": The pivotal tracker API URL (e.g. "https://www.pivotaltracker.com/services/v5")
* "TOKEN_HEADER": This is the name of the header that will contain the token (e.g. "X-TrackerToken")
* "PREFIX": This prefix will be used on all created projects and also to delete all data that was generated by testing tool.
* "USER": This is a list of users. By default it expects one owner and two members (working on the same account). 
You can find your user TOKEN and ID on the User settings in Pivotal Tracker page (e.g. "https://www.pivotaltracker.com/profile"). 
If you don't find the id you can always request it.
* "ACCOUNT_ID": The account id the users are working on. It can be found on the account settings.
* "PATH_DATA_FILES": You can use customized test data. If you don't know how to configure this or what files are required 
you can fill this with "/pivotal_tracker/features/test_data". If customized testing is being done please create all files for testing.
* "Content-Type": This depends on the type of request we are sending. If not customized please use "application/java".

After filling all these field you can change the configuration file name "config.dist" -> "config.json". 
Once we do this we are good to go for some testing. 

To test all Pivotal Tracker Features, you can simply go to the project folder and run from your terminal: **python3 test_pivotal_tracker.py**
