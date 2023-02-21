from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_basics(self):
        self.open("https://github.com/")

        # after landing on the main page, search "react" in the search bar
        
        # go through languages filter and verfy results

        # clear the filter and go to facebook/react repo and verfy some page elements
        
        # navigate through different tabs of the repo (e.g. Issues, Pull requests, etc.)

        # hover over on the main navigation and verfy the dropdown content (e.g. Product, Solutions, etc)

        ## Extra ##
        ## write any tests you find interesting, don't go too wild :)
