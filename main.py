from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



with webdriver.Firefox(executable_path='geckodriver.exe') as driver:

    wait = WebDriverWait(driver, 10)
    driver.get("https://eservices.ejar.sa/ar/public/login")
    driver.find_element_by_name("current_username").send_keys("1111111111")
    driver.find_element_by_name("current_password").send_keys("Password here" + Keys.RETURN)

    wait.until(presence_of_element_located((By.CSS_SELECTOR, "ALHASHIM")))

    


   
   
   

   

 
