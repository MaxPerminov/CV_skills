import time


class Login:
  @staticmethod
  def logvin(service, manager, webdriver, path,
   by_login, value_login, login,
    by_password, value_password, password,
     by_submit, value_submit):
  
    service = service(
      executable_path=manager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(path)
    time.sleep(3)

    for i in range(len(login)):
      login_field = driver.find_element(by=by_login, value=value_login)
      login_field.send_keys(login[i])

      pass_field = driver.find_element(by=by_password, value=value_password)
      pass_field.send_keys(password[i])

      button = driver.find_element(by=by_submit, value=value_submit)
      button.click()      
      time.sleep(3)

      driver.refresh()

      
    driver.quit()
