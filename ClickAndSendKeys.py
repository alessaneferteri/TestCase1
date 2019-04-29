from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestPage():
       
    def HomePage(self):
        baseURL = "http://automationpractice.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        
        loginLink = driver.find_element(By.XPATH, "//a[@title='Log in to your customer account']")
        ActionChains(driver).move_to_element(loginLink).perform()
        time.sleep(2)
        
        contactUs = driver.find_element(By.XPATH, "//a[@title='Contact Us']")
        ActionChains(driver).move_to_element(contactUs).perform()
        time.sleep(2)
        
        loginLink.click()
        time.sleep(3)
        
        driver.find_element(By.ID, "email").send_keys("hanjeun90@gmail.com")
        time.sleep(3)
        
        driver.find_element(By.ID, "passwd").send_keys("Claym0r#01")
        time.sleep(3)
        
        driver.find_element(By.XPATH, "//p[@class='submit']//span[1]").click()
        time.sleep(3)
        
        driver.find_element(By.NAME, "email_create").send_keys("hanjeun90@gmail.com")
        time.sleep(3)
        
        driver.find_element(By.XPATH, "//form[@id='create-account_form']//span[1]").click()
        time.sleep(3)
        driver.find_element(By.ID, "id_gender1").click()
        time.sleep(3)
        driver.find_element(By.ID, "id_gender2").click()
        driver.find_element(By.XPATH, "//input[@id='customer_firstname']").send_keys("Alessa Neferteri")
        time.sleep(3)
        
        driver.quit()
        
ch = TestPage()
ch.HomePage()