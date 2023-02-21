# seleniumbase-qa-interview
This is based off and using www.seleniumbase.io

# Pre-requisites
Having the following installed
* python
* pip
* seleniumbase.io

Selenium base has good documentation how to install python, pip and sbase here (This will also take care of all webdriver needs)
https://seleniumbase.io/help_docs/install_python_pip_git/

From there you can install seleniumbase with pip: ```pip install seleniumbase```

# Fork this project and create a pull request on your own repo and send me the link.
# Don't spend too much time on this, it's expected to be done within 1-2 hours

# Write the following test cases for MyTestClass(BaseCase):
```
class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://github.com/")
        
    # after landing on the main page, search "react" in the search bar
        
    # click on the filter dropdown to go through different filters and perform some tesing.

    # clear the filter and go to facebook/react repo and verify some page elements
    
    # navigate through different tabs of the repo (e.g. Issues, Pull requests, etc.)

    # hover over on the main navigation and verify the dropdown content (e.g. Product, Solutions, etc)

    ## Extra ##
    ## write any tests you find interesting, don't go too wild :)
 ```

# How to run the test file
```
pytest qa_interview_test.py      
```

# Useful documentation link
https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/fixtures/base_case.py
