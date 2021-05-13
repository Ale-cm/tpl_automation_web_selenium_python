#FROM: https://www.selenium.dev/selenium/docs/api/py/index.html
from pa_lib import BaseTest

class TestEjemplo(BaseTest):
    def testPageTitleOk(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def testPageTitleFalla(self):
        self.browser.get('http://www.google.com')
        self.assertIn('este NO PUEDE ser EL TITULO', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)


