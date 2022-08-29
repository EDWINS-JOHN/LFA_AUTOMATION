import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import  LogGen


class Test_01_Login:
    baseURL = ReadConfig.getAppUrl()
    phone = ReadConfig.getPhone()
    password = ReadConfig.getPassword()
    
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        
        self.logger.info("*******************Test_01_Login************")
        self.logger.info("*******************Checking  Homepage Title************")
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        if actual_title == "Lori Field App":
            assert True
            self.driver.close()
            self.logger.info("*******************Test passed************")
        else:
            self.driver.save_screenshot("..\\ScreenShots\\"+"test_homePagetitle.png")
            self.driver.close()
            assert False
            
    
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setPhoneNumber(self.phone)
        self.login.setPassword(self.password)
        self.login.click_login()
        page_title =self.driver.title
        if page_title == "Lori Field App":
            assert True
            self.driver.close()
            self.logger.info("*******************Login Test Passed************")
        else:
            self.driver.save_screenshot("..\\ScreenShots\\"+"test_login.png")
            self.driver.close()
            assert False