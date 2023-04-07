from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.common.by import By

from selen_chrome_methods.selen_chrome_methods import Meths
from class_iterator.class_iterator import Class_iterator
from get_paramtr.get_parametr import Get_parametr
from methods_to_list.methods_to_list import Method_to_list
from options_to_dict.options_to_dict import Options_to_dict


## methods will run in alphabetical order, so parameters must be corresponded
## replace parameters, that are with less/greater signs, on actual parameters

parameters = [
  (ChromeService, ChromeDriverManager, webdriver, "<path>", "<By.?>", "<by_value>"),          # for @staticmethod clicker
  (ChromeService, ChromeDriverManager, webdriver, "<path>"),                                  # for @staticmethod get
  (ChromeService, ChromeDriverManager, webdriver, "<path>"),                                  # for @staticmethod screener
  (ChromeService, ChromeDriverManager, webdriver, "<path>", "<By.?>", "<by_value>", "<text>") # for @staticmethod typer
   ]

method_list =  Method_to_list.methods_to_list(Meths)
options  = Options_to_dict.options_to_dict(method_list, parameters)

cl_iterator = Class_iterator.class_iterator
gt_pam = Get_parametr.get_paramtr


if __name__ == "__main__":

  cl_iterator(gt_pam, options, Meths)
    