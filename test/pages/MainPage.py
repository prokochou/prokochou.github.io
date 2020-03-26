from .BasePage import BasePage
from .BasePage import IncorrectPageExpection
from UIMap import HomePageMap


class MainPage(object):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.assertEqual(self.driver.title, "Proko's Blog")
        except:
            raise IncorrectPageExpection

    def _about_me_button_click(self):
        button = BasePage.wait_until_element_clickable(self, 10, "xpath", HomePageMap['AboutMeXpath'])
        button.click()

    def _work_button_click(self):
        button = BasePage.wait_until_element_clickable(self, 10, "xpath", HomePageMap['WorkXpath'])
        button.click()

    def _talks_button_click(self):
        button = BasePage.wait_until_element_clickable(self, 10, "xpath", HomePageMap['TalksXpath'])
        button.click()

    def _linked_in_button_click(self):
        button = BasePage.wait_until_element_clickable(self, 10, "xpath", HomePageMap['LinkedInXpath'])
        button.click()

