import time


class Meths:

  @staticmethod
  def clicker(service, manager, webdriver, path,
   by_, value):
  
    service = service(
      executable_path=manager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(path)
    button = driver.find_element(by_, value)
    button.click()
    time.sleep(3)      
    driver.quit()


  @staticmethod
  def get(service, manager, webdriver, path):
    
    service = service(
      executable_path=manager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(path)
    driver.quit()    


  @staticmethod
  def screener(service, manager, webdriver, path):
    
    service = service(
      executable_path=manager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(path)
    driver.save_screenshot(f"scr{time.time()}.png")
    driver.quit()


  @staticmethod
  def typer(service, manager, webdriver, path,
    by_, value, text):

    service = service(
      executable_path=manager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(path)
    time.sleep(2)
    field = driver.find_element(by_, value)
    field.send_keys(text)      
    time.sleep(2)
    driver.quit()
