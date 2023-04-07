from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import time


class FakeUaDriver:
    def __init__(self, mask):
        op = webdriver.ChromeOptions()
        op.add_argument(f'user-agent={mask}')
        self.driver = webdriver.Chrome(options=op,
                                       service=ChromeService(ChromeDriverManager().install()))


# new random ua instance
random_driver = FakeUaDriver(UserAgent().random)

# adding cookies

random_driver.driver.get("https://www.whatismybrowser.com/ ")
random_driver.driver.add_cookie({"name": "name", "value": "John"})
random_driver.driver.add_cookie({"name": "surname", "value": "Doe"})
random_driver.driver.add_cookie({"name": "age", "value": "23"})
time.sleep(30)

random_driver.driver.quit()
