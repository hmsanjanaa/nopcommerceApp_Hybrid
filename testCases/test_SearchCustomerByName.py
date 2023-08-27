import logging
import time
import pytest
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********** Search Customer By Name_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successful *****")
        self.logger.info("***** Searching Customer with First Name and Last Name *****")

        # Navigate to Customers from menu
        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()

        # Search Customer using email
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clicksearch()
        time.sleep(5)
        status = searchcust.searchcustomerbyName("Victoria Terces")
        assert True == status
        self.logger.info("***** Test_SearchCustomerByName_004 Finished *****")
        self.driver.close()
