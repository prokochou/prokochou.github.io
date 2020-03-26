from Constants import TT_Constants
from BestTestCase import BestTestCase
from pages.MainPage import MainPage
import unittest
import nose
from nose.plugins.attrib import attr
from pages.BasePage import BasePage


class CheckButton(unittest.TestCase):

    def setUp(self):
        super(CheckButton, self).setUp()
        BestTestCase.setup(self)
        BestTestCase.navigate_to_page(self, TT_Constants["Base_URL"])

    @attr(priority="high")
    def test_aboutMe_button(self):
        MainPage._about_me_button_click(self)
        url = BestTestCase.get_current_url(self)
        self.assertEqual(url, "https://prokochou.github.io/#about")

    def test_work_button(self):
        MainPage._work_button_click(self)
        url = BestTestCase.get_current_url(self)
        self.assertEqual(url, "https://prokochou.github.io/#works")

    def test_talks_button(self):
        MainPage._talks_button_click(self)
        url = BestTestCase.get_current_url(self)
        self.assertEqual(url, "https://prokochou.github.io/#talks")

    def test_linkedIn_button(self):
        MainPage._linked_in_button_click(self)
        BasePage.switch_to_window(self)
        url = BestTestCase.get_current_url(self)
        self.assertEqual(url, "https://www.linkedin.com/in/proko-chou-5803ab26/")

    def tearDown(self):
        BasePage.quit(self)


if __name__ == '__main__':
    nose.main()
