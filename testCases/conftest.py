import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time
from datetime import datetime

@pytest.fixture()
def setup():
        driver= webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
        return driver

#@pytest.fixture()
#def setup():
 #   driver = webdriver.Chrome()
  #  return driver

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
#def pytest_configure(config):
#    config._metadata['Project Name'] = 'SeleniumPytest'
#    config._metadata['Module Name'] = 'TestDemo'
#    config._metadata['Tester'] = 'Sayali'

# It is hook for delete/Modify Environment info to HTML Report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#    metadata.pop("JAVA_HOME", None)#
#    metadata.pop("Plugins", None)