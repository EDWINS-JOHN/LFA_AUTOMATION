import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_01_Login:
    baseURL="https://tsavo.welovetrucks.co/login/"
    phone = "716258644"
    password ="gigi-Mamba2006"

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        if actual_title == "Lori Field App":
            assert True
            self.driver.close()
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
        else:
            self.driver.save_screenshot("..\\ScreenShots\\"+"test_login.png")
            self.driver.close()
            assert False