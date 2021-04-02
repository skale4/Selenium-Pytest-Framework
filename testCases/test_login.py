from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
#from utilities.readProperties import ReadConfig
from utilities import config as environment
import allure


class Test_001_Login:
    baseURL = environment.BaseURL
    username = environment.UserEmail
    password = environment.Password
    logger = LogGen.loggen()

  #  @pytest.mark.regression
    @allure.description("This is to check title of the login page")
    @allure.severity(severity_level="NORMAL")
    def test_homePageTitle(self,setup):
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
    @allure.description("This is to check login testcase")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration222":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".//Screenshots//" + "test_LoginPageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_LoginPageTitle222.png1", attachment_type=allure.attachment_type.PNG)
            self.driver.close()
            assert False





