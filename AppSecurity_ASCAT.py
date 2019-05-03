'''
Created on May 3, 2019

@author: alessa.n.c.batino
'''
import unittest, time
from selenium import webdriver

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testNgURL(self):        
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get("http://d14hbg6jh4y4dz.cloudfront.net")
        time.sleep(2)
        driver.get("http://ascat.dev.net.s3-website-ap-northeast-1.amazonaws.com")
        time.sleep(2)
        driver.get("https://s3-ap-northeast-1.amazonaws.com/ascat.dev.net/index.html")
        time.sleep(2)
    
    def testOkURL(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get("https://d14hbg6jh4y4dz.cloudfront.net")
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()