import pytest
from selenium import webdriver
import logging
from datetime import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    log = LogGen.loggen(logLevel=logging.INFO)

    def test_homePageTitle(self, setup):
        self.log.info("********************** Test_001_Login *********************************")
        self.log.info("********************* Verifying HomePage Title ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.log.info("********************* HomePage Title test PASSED ************************")

        else:
            self.log.error("********************* HomePage Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.log.info("********************** Test_001_Login *********************************")
        self.log.info("********************* Verifying Login Title ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.log.info("********************* LoginPage Title test PASSED ************************")
        else:
            self.log.error("********************* LoginPage Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
