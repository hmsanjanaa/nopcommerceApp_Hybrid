import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random
import logging


class Test_003_AddCustomer:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen(logLevel=logging.INFO)
    # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")
        self.logger.info("******* Starting Add Customer Test **********")
        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("************* Providing customer info **********")

# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
        # user_defined random_generator function below:
        self.email = random_generator() + "@gmail.com"
        # print(self.email)
        self.addcust.setEmail(self.email)
        self.logger.info("********** Email entered **********")
        self.addcust.setPassword('text123')
        self.logger.info("********** Password entered **********")
        self.addcust.setFirstName('ShowOff')
        self.logger.info("********** FirstName entered **********")
        self.addcust.setLastName('Automation')
        self.logger.info("********** Last Name entered **********")
        self.addcust.setGender('Female')
        self.logger.info("********** Gender Selected **********")
        self.addcust.setDob('06/17/1994')
        self.logger.info("********** DOB entered **********")
        self.addcust.setCompanyName('SomeCompany')
        self.logger.info("********** Company entered **********")
        self.addcust.setCustomerRoles('Guests')
        self.logger.info("********** Customer roles selected **********")
        self.addcust.setManagerOfVendor('Vendor 1')
        self.logger.info("********** Vendors selected **********")

        self.addcust.setAdminContent('Adding Comments')
        self.logger.info("********** Comments entered **********")
        self.addcust.clickOnSave()
        time.sleep(5)
        self.logger.info("********** Clicked on save **********")

        self.logger.info("********** Saving Customer Info **********")
        #self.msg = self.driver.find_element(By.CLASS_NAME, "alert alert-success alert-dismissable")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
       # print(self.msg)
        time.sleep(5)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot("./Screenshots/add_Customer_Scr.png")
            self.logger.info("********** Add Customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Add Customer Test **********")

def random_generator(size=8,
                         chars=string.ascii_lowercase + string.digits):  # generates 8 characters with letters and digits
        x = ''.join(random.choice(chars) for x in range(size))  # everytiome new character string
        print(x)
        return x