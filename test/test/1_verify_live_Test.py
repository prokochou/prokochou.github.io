import __init__
from Constants import TT_Constants
from Constants import LocatorMode
from BestTestCase import BestTestCase
from pages.MainPage import MainPage
from pages.BasePage import BasePage
import unittest
import nose
from nose.plugins.attrib import attr


class CheckLive(unittest.TestCase):

    def setUp(self):
        super(CheckLive, self).setUp()
        BestTestCase.setup(self)
        BestTestCase.navigate_to_page(self, TT_Constants["Base_URL"])

    @attr(priority="high")
    def test_checkLive(self):
        MainPage._verify_page(self)

    def tearDown(self):
        BasePage.quit(self)


if __name__ == '__main__':
    nose.main()
