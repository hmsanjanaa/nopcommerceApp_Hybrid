from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome Browser.......")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox Browser.......")
    else:  # Default driver
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        print("Launching Edge Browser.......")
    return driver

   
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Module Name": "Customers",
        "Tester": "Sanjana",
        "Project Name": "nop Commerce",
    }


# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
