import pytest
from selenium import webdriver



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
       driver = webdriver.Chrome()
       print("Launching Chrome browser.......")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching FireFox browser........")

    else:
        driver = webdriver.Chrome()
    return driver



def pytest_addoption(parser):   # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

################## Pytest HTML Report ######################

#It is hook for adding enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Constantin'

# It is hook for delete /Modify Enviroment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)