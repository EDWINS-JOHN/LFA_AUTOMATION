from selenium.webdriver.common.by import By
class LoginPage:
    
       input_phone_id ="phone"
       input_password_id="password"
       login_button_xpath ="//span[contains(text(),'Log In')]"
       menu_button_xpath ="//button[@aria-label='Menu']"
       sign_out_xpath ="//span[normalize-space()='Sign Out']"
       
       
       def __init__(self,driver):
              self.driver=driver
              
              
              
       def setPhoneNumber(self,phone):
              self.driver.find_element(By.ID,self.input_phone_id).clear()
              self.driver.find_element(By.ID,self.input_phone_id).send_keys(phone)
              
       def setPassword(self,password):
              self.driver.find_element(By.ID,self.input_password_id).clear()
              self.driver.find_element(By.ID,self.input_password_id).send_keys(password)
              
              
       def click_login(self):
              self.driver.find_element(By.XPATH,self.login_button_xpath).click()
              
       def svgMenu(self):
              self.driver.find_element(By.XPATH,self.menu_button_xpath).click()
              
       def signOut(self):
              self.driver.find_element(By.XPATH,self.sign_out_xpath).click()