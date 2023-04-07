from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from get_page.get_page import Get_page
from tests_registration.registration_tests import Reg
from tests_login.login_tests import Login



if __name__ == "__main__":

  #################################################################################
  # Testing of getting page:

  # IT'S NECESSARILY TO CHANGE <TDD> PARAMETER
  Get_page.get(ChromeService, ChromeDriverManager, webdriver, "http:<TDD>")

  #################################################################################
  # Testing registration:

  emails = [
    "max_len_email@gulge.com", 
    "min_len_email@gulge.com", 
    "regular@gulge.com",
    "regular@gulge.com",
    "regular@gulge.com",
    ""
    "regular@gulge.com",
    "",
    "    ",
    "regulargulge.com"
    ]

  passwords = [
    "regular_password",
    "regular_password",
    "max_password",
    "min_password",
    ""
    "",
    "    ",
    "regular_password",
    "regular_password",
    "regular_password",
    ]
    
  # IT'S NECESSARILY TO CHANGE <TDD> PARAMETER
  Reg.registration(ChromeService, ChromeDriverManager, webdriver, "http:<TDD>", By.<TDD>, "<TDD>",
                    emails, By.<TDD>, "<TDD>", passwords, By.<TDD>, "<TDD>")

  #################################################################################
  #Testing login:

  logins = [
    "valid_login",
    "",
    "valid_login",
    "valid_login",
    "valid_login",
    "",
    "invalid_password",
    "    ",
    "valid_login"
    ]

  passwords = [
    "valid_password",
    "",
    "",
    "invalid_password",
    "    ",
    "valid_password",
    "valid_password",
    "valid_password",
    "valid_login"
  ]

  # IT'S NECESSARILY TO CHANGE <TDD> PARAMETER
  Login.logvin(ChromeService, ChromeDriverManager, webdriver, "http:<TDD>", By.<TDD>, "<TDD>",
                logins, By.<TDD>, "<TDD>", passwords, By.<TDD>, "<TDD>")
