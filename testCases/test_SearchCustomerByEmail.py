import logging
import time
import pytest
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.regression
    def test_searchcustomeby_email(self, setup):
        self.logger.info("************** search by email_004 *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********** login successfully *************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info('**********************  Start search customer by Email test  **************')
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setemail("victoria_victoria@nopCommerce.com")
        self.searchcust.clicksearch()
        time.sleep(5)
        status = self.searchcust.searchcustomerbyemail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("******** search by email finished ********")
        self.driver.close()
