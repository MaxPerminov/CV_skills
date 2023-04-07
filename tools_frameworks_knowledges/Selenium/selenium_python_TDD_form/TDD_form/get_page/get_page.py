class Get_page:
  @staticmethod
  def get(service, manager, webdriver, path):
    
    service = service(
      executable_path=manager().install())

    driver = webdriver.Chrome(service=service)
    driver.get(path)
    
    driver.quit()
