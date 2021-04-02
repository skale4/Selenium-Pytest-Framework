import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
#from utilities.readProperties import ReadConfig
from utilities import config as environment
from utilities.read_xlsx_data import XlsxReader
from utilities.write_xlsx_data import XlsxWriter


class Test_001_Login:
    baseURL = environment.BaseURL
    #username = environment.UserEmail
    #password = environment.Password
    logger = LogGen.loggen()


  #  @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            assert False

   # @pytest.mark.sanity
   # @pytest.mark.regression
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_login_data())
    def test_login(self, setup, data):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(data.username)
        self.lp.setPassword(data.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".//Screenshots//" + "test_LoginPageTitle.png")
            self.driver.close()
            assert False





