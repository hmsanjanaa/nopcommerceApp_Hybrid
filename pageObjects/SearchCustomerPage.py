import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SearchCustomer:
    txtEmail_id = 'SearchEmail'
    txtFirstName_id = 'SearchFirstName'
    txtLastname_id = 'SearchLastName'
    btnSearch_id = 'search-customers'

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tablerows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tablecols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastname_id).clear()
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lastname)

    def getNumofrows(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerows_xpath))

    def getColnum(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecols_xpath))

    def searchcustomerbyemail(self, email):
        flag = False
        for r in range(1, self.getNumofrows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchcustomerbyName(self, Name):
        flag = False
        for r in range(1, self.getNumofrows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag

    def clicksearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()
