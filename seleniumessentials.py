from Selenium2Library import Selenium2Library
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
import json
import time
import string
import random
from Selenium2Library import Selenium2Library
from selenium.webdriver.common.action_chains import ActionChains


# create new class that inherits from Selenium2Library
class SeleniumEssentials:
    """
    SeleniumEssentials class contains customised library functions which are either extended or customised
    to cater the need of various ui automation tasks
    """

    def __init__(self):
        self.builtin = BuiltIn()

    # create a new keyword called "get webdriver instance"
    def get_webdriver_instance(self):
        """this function will return the current browser instance object """
        sel = self.builtin.get_library_instance('Selenium2Library')._current_browser()
        return sel

    def wait_for_presence_of_element_located(self, driver, element_locator, timeout=15):

        """wait_for_element function is used to explicitly wait for a specified time for the element to be present,
         else would return timeout exception"""

        try:
            element_present = EC.presence_of_element_located((By.XPATH, element_locator))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException, err:
            raise TimeoutException(
                "Timed out..taking too long to find the element {} on the page...".format(element_locator))

    def wait_for_visiblity_of_element_located(self, driver, element_locator, timeout=15):

        """wait_for_element function is used to explicitly wait for a specified time for the element to be visibile,
         else would return timeout exception"""

        try:
            element_visible = EC.visibility_of_element_located((By.XPATH, element_locator))
            WebDriverWait(driver, timeout).until(element_visible)
        except TimeoutException, err:
            raise TimeoutException(
                "Timed out..taking too long to find the element {} on the page...".format(element_locator))

    def wait_for_invisibility_of_element_located(self, driver, element_locator, timeout=15):

        """wait_for_element function is used to explicitly wait for a specified time for the element to be invisibile,
         else would return timeout exception"""

        try:
            element_invisible = EC.visibility_of_element_located((By.XPATH, element_locator))
            WebDriverWait(driver, timeout).until(element_invisible)
        except TimeoutException:
            raise TimeoutException(
                "Timed out..taking too long to find the element {} on the page...".format(element_locator))

    def wait_for_text_to_be_present_in_element(self, driver, element_locator, timeout=15):

        """wait_for_element function is used to explicitly wait for a specified time for the element text to be present,
         else would return timeout exception"""

        try:
            element_text_present = EC.text_to_be_present_in_element((By.XPATH, element_locator))
            WebDriverWait(driver, timeout).until(element_text_present)
        except TimeoutException:
            raise TimeoutException(
                "Timed out..taking too long to find the element {} on the page...".format(element_locator))

    def wait_for_frame_to_be_available_and_switch_to_it(self, driver, element_locator, timeout=15):

        """wait_for_element function is used to explicitly wait for a specified time for the frame to be available and switch to_it
         present, else would return timeout exception"""

        try:
            frame_available = EC.frame_to_be_available_and_switch_to_it((By.XPATH, element_locator))
            WebDriverWait(driver, timeout).until(frame_available)
        except TimeoutException:
            raise TimeoutException(
                "Timed out..taking too long to find the element {} on the page...".format(element_locator))

    def wait_for_element_to_be_clickable(self, driver, element_locator, timeout=15):

        """wait_for_element function is used to explicitly wait for a specified time for the element to be clickable,
         else would return timeout exception"""

        try:
            element_clickable = EC.element_to_be_clickable((By.XPATH, element_locator))
            WebDriverWait(driver, timeout).until(element_clickable)
        except TimeoutException, err:
            raise TimeoutException(
                "Timed out..taking too long to find the element {} on the page...".format(element_locator))

    def wait_post_refresh(self,driver,element_locator, timeout_int=5):
        try:
            print ("Checking if the value is present before refresh")
            element = driver.find_element(By.XPATH, element_locator)
            if element is True:
                print ("Element present before refresh")

            time_int = 0
            while time_int <= timeout_int:
                try:
                    print ("Refreshing")
                    driver.find_element_by_xpath("//span[@class='refresh-container']/i").click()
                    #SE.move_to_element_by_xpath(driver, critical_issue_xpaths['critical_issue_tab'])
                    #driver.find_element_by_xpath(critical_issue_xpaths['critical_issue_tab']).click()
                    print ("Checking if the value is present post refresh")
                    element = driver.find_element(By.XPATH, element_locator)
                    if element is True:
                        return True
                except Exception as e:
                    time_int += 1
                    print "Sleep for 10 seconds in iteration " + str(time_int)
                    time.sleep(10)
            return False

        except Exception, err:
            raise err

    def move_to_element_by_xpath(self,driver,xpath,direction=None):
       try:
            if direction == 'up':
                driver.execute_script('window.scrollTo(0,0)')
                time.sleep(2)

            element = driver.find_element_by_xpath(xpath)
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            #driver.execute_script('return window.pageYOffset')
            #driver.execute_script("return document.body.scrollHeight")
            #driver.execute_script('window.scrollBy(0,50)')
            #driver.execute_script('window.scrollBy(0,-50)')
            driver.execute_script('window.scrollBy(0,50)')
       except Exception as e:
           raise e + 'Element not present:' + xpath

    def get_authorisation_token(self):
        ab = self.builtin.get_library_instance('Selenium2Library')._current_browser()
        ab.session_id()

    def generateRandomText(self,number_of_characters):
        try:
             if number_of_characters == None:
                 raise ("Please provide an input")
             elif number_of_characters == 0:
                 raise("Please give a number greater the zero")
             else :
                 chars = "".join([random.choice(string.letters) for i in xrange(int(number_of_characters))])
                 if len(chars) != number_of_characters:
                     print "Number of characters asked:" + str(number_of_characters)
                     print "Number of characters generated:" + str(len(chars))
                     raise("Please check there is some issue with generating random text")
                 else:
                     print "Number of characters generated are:" + str(len(chars))
                     print "Generated text:=" + str(chars) + "="
                     return chars

        except Exception as e:
            print e
