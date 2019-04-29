from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing-hp-flight")
        # Click departing field
        departingField.click()

        time.sleep(3)
        driver.quit()

ff = CalendarSelection()
ff.test1()