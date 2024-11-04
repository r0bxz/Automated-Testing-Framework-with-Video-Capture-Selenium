from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.test_data import TestData
from selenium.common.exceptions import StaleElementReferenceException
import time

class EmployeePage:
    def __init__(self, driver):
        self.driver = driver
    report_to_tab = (By.XPATH, "//a[text()='Report-to']")
    PIM = (By.CLASS_NAME, "oxd-main-menu-item")  
    EMPLOYEE_LIST = (By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")  
    ADD_BUTTON = (By.CLASS_NAME, "oxd-button")  
    SAVE_BUTTON=(By.CLASS_NAME,"oxd-button")
    input_fields = (By.CLASS_NAME, "oxd-input") 
    profile_picture =(By.CLASS_NAME,"oxd-file-input")
    items =(By.CLASS_NAME,"orangehrm-tabs-item")
    select = (By.CLASS_NAME,"oxd-select-text")
    drop_down=(By.CLASS_NAME,"oxd-select-option")
    pagenation=(By.CLASS_NAME,"oxd-pagination-page-item")
    supervisor_name_field=(By.CSS_SELECTOR, "div.oxd-autocomplete-text-input--active input[placeholder='Type for hints...']")
    autocomplete_dropdown_options=(By.CLASS_NAME,"oxd-autocomplete-dropdown")
    supervisor_option=(By.XPATH, "//div[contains(@class, 'oxd-autocomplete-text-input')]/following-sibling::div//span")
    reporting_method=(By.CLASS_NAME,"oxd-select-text")
    
   
    def add_supervisor(self,first_name,last_name,supervisor_id,photo_path):
        self.driver.find_elements(*self.PIM)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.EMPLOYEE_LIST)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.ADD_BUTTON)[2].click()
        time.sleep(1)
        self.driver.find_elements(*self.input_fields)[1].send_keys(first_name)
        time.sleep(1)
        self.driver.find_elements(*self.input_fields)[3].send_keys(last_name)
        time.sleep(1)
        self.driver.find_element(*self.profile_picture).send_keys(photo_path)
        self.driver.find_elements(*self.input_fields)[4].send_keys(Keys.CONTROL + "a")
        self.driver.find_elements(*self.input_fields)[4].send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_elements(*self.input_fields)[4].send_keys(supervisor_id)
        time.sleep(1)
        self.driver.find_elements(*self.SAVE_BUTTON)[1].click()
        time.sleep(1)
        
    def add_employee(self, first_name,last_name, employee_id, photo_path):
        self.driver.find_elements(*self.PIM)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.EMPLOYEE_LIST)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.ADD_BUTTON)[2].click()
        time.sleep(1)
        self.driver.find_elements(*self.input_fields)[1].send_keys(first_name)
        time.sleep(1)
        self.driver.find_elements(*self.input_fields)[3].send_keys(last_name)
        time.sleep(1)
        self.driver.find_element(*self.profile_picture).send_keys(photo_path)
        self.driver.find_elements(*self.input_fields)[4].send_keys(Keys.CONTROL + "a")
        self.driver.find_elements(*self.input_fields)[4].send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_elements(*self.input_fields)[4].send_keys(employee_id)
        time.sleep(1)
        self.driver.find_elements(*self.SAVE_BUTTON)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.items)[5].click()
        time.sleep(1)
        self.driver.find_elements(*self.select)[0].click()
        time.sleep(1)
        
        
        
        options = self.driver.find_elements(*self.drop_down)
        for option in options:
            try:
             if(TestData.job_title in option.text):
                option.click()
                break
            except StaleElementReferenceException:
               time.sleep(1)
        self.driver.find_elements(*self.SAVE_BUTTON)[0].click()
        time.sleep(1)
        self.driver.find_element(*self.report_to_tab).click()
        time.sleep(1)
        self.driver.find_elements(*self.ADD_BUTTON)[0].click()
        time.sleep(1)
        self.driver.find_element(*self.supervisor_name_field).send_keys(TestData.SUPERVISOR_FIRST_NAME)
        self.driver.find_element(*self.supervisor_option).click()
        time.sleep(1)
        
        self.driver.find_element(*self.reporting_method).click()
        options = self.driver.find_elements(*self.drop_down)
        for option in options:
            try:
             if(TestData.reporting_method in option.text):
                option.click()
                break
            except StaleElementReferenceException:
               time.sleep(1)
        self.driver.find_elements(*self.SAVE_BUTTON)[1].click()
        time.sleep(1)
        
    def verify_employee_added(self, id_number):
        self.driver.find_elements(*self.EMPLOYEE_LIST)[1].click()
        time.sleep(5)
        if id_number in self.driver.page_source:
         print(f"Employee with '{id_number}' was added successfully!")
        else:
         pagination_elements = self.driver.find_elements(*self.pagenation)
         page=1
         while(page < len(pagination_elements)):
             try:
              pagination_elements[page].click()  
              page += 1
              time.sleep(4)
              if id_number in self.driver.page_source:
                print(f"Employee with '{id_number}' was added successfully!")
                break
             except StaleElementReferenceException:
                time.sleep(1)
        

