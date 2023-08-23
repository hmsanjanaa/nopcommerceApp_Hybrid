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
        # result = ''.join((random.choice(string.ascii_lowercase + string.digits) for x in range(8)))
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Sanjanaa")
        self.addcust.setLastName("H")
        self.addcust.setDob("01/05/1993")  # Format: D / MM / YYY
        self.addcust.setCompanyName("QA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()
        # self.actAddCustomer.setEmailToCustomer(result + ".gmail.com")
        # self.actAddCustomer.setPasswordToCustomer("1234")
        # self.actAddCustomer.setFirstNameToCustomer("Avi")
        # self.actAddCustomer.setLastNameToCustomer("Band")
        # self.actAddCustomer.clickgenderMaleRadioButton()
        # self.actAddCustomer.setDateofbarth("4/6/2023")
        # self.actAddCustomer.setCompanyName("student")
        # self.actAddCustomer.clickIsTaxExemptChechedBox()
        # self.actAddCustomer.clickNewsletterClickEmpty()
        # self.actAddCustomer.clicknewseletterYourstorename()
        # self.actAddCustomer.clickCustomerrolesClickEmpty()
        # self.actAddCustomer.clickCustomerrolesAdministrators()
        # # self.actAddCustomer.selectManagerofvendor("Vendor 1")
        # self.actAddCustomer.setAdmincomment("It's Google.")
        # self.actAddCustomer.clicksaveButtonButton()
        # flag = self.actAddCustomer.VerifyAddCustomerSuccessfullymassage()
        # print("##################################   "+flag)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
