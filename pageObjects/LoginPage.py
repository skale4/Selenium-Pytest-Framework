from locators.locators import SetLoginPageLocators

class LoginPage:
    # Login Page
    textbox_username_id = SetLoginPageLocators.textbox_username
    textbox_password_id = SetLoginPageLocators.textbox_password
    button_login_xpath =  SetLoginPageLocators.button_login
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(*SetLoginPageLocators.textbox_username).clear()
        self.driver.find_element(*SetLoginPageLocators.textbox_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*SetLoginPageLocators.textbox_password).clear()
        self.driver.find_element(*SetLoginPageLocators.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*SetLoginPageLocators.button_login).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()