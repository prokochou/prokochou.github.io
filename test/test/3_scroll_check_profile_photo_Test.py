from Constants import TT_Constants
from BestTestCase import BestTestCase
from pages.MainPage import MainPage
import unittest
import nose
from nose.plugins.attrib import attr
from pages.BasePage import BasePage


class CheckProfilePhoto(unittest.TestCase):

    def setUp(self):
        super(CheckProfilePhoto, self).setUp()
        BestTestCase.setup(self)
        BestTestCase.navigate_to_page(self, TT_Constants["Base_URL"])

    @attr(priority="low")
    def test_check_profile_photo(self):
        # Scroll to AboutMe
        MainPage._about_me_button_click(self)
        url = BestTestCase.get_current_url(self)
        self.assertEqual(url, "https://prokochou.github.io/#about")

        # Take Photos' screenshots
        count = 4
        for i in range(count):
            filename = "screenshot/AboutMe_" + BasePage.timestamp(self) + ".png"
            BasePage.screenshot(self, filename)
            BasePage.wait_aboutme_photo_change(self, 5)

    def tearDown(self):
        BasePage.quit(self)


if __name__ == '__main__':
    nose.main()