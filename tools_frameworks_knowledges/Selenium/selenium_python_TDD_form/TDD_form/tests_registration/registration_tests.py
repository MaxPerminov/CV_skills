import time


class Reg:
  @staticmethod
  def registration(service, manager, webdriver, path,
   by_email, value_email, email,
    by_password, value_password, password,
     by_submit, value_submit):
  
    service = service(
      executable_path=manager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(path)
    time.sleep(3)

    for i in range(len(email)):
      email_field = driver.find_element(by=by_email, value=value_email)
      email_field.send_keys(email[i])

      pass_field = driver.find_element(by=by_password, value=value_password)
      pass_field.send_keys(password[i])

      button = driver.find_element(by=by_submit, value=value_submit)
      button.click()      
      time.sleep(3)

      driver.refresh()
    
    
    driver.quit()
