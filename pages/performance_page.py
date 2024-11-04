from selenium.webdriver.common.by import By
from data.test_data import TestData
from selenium.common.exceptions import StaleElementReferenceException
import time

class PerformancePage:
    def __init__(self, driver):
        self.driver = driver
        self.Performance= (By.CLASS_NAME, "oxd-main-menu-item") 
        self.menu_item= (By.CLASS_NAME,"oxd-dropdown-menu")
        self.tab_item= (By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")
        self.kpi_name=(By.CLASS_NAME,"oxd-input")
        self.date_inputs=(By.CLASS_NAME,"oxd-input")
        self.button = (By.CSS_SELECTOR, ".oxd-button")
        self.drop_down=(By.CLASS_NAME,"oxd-select-text")
        self.manage_reviews=(By.XPATH, "//a[text()='Manage Reviews']")
        self.options=(By.CLASS_NAME,"oxd-select-option")
        self.name_fields=(By.CSS_SELECTOR, "div.oxd-autocomplete-text-input--active input[placeholder='Type for hints...']")
        self.option=(By.XPATH, "//div[contains(@class, 'oxd-autocomplete-text-input')]/following-sibling::div//span")

    def assign_review(self, employee_name, reviewer_name, comment):
        self.driver.find_element(*self.employee_field).send_keys(employee_name)
        self.driver.find_element(*self.reviewer_field).send_keys(reviewer_name)
        self.driver.find_element(*self.review_comment_field).send_keys(comment)
        self.driver.find_element(*self.save_button).click()
        
    def add_kpi(self,name,job_title):
        self.driver.find_elements(*self.Performance)[6].click()
        time.sleep(1)
        self.driver.find_elements(*self.tab_item)[0].click()
        time.sleep(1) 
        self.driver.find_elements(*self.menu_item)[0].click()
        time.sleep(1) 
        self.driver.find_elements(*self.button)[2].click() #add button 
        time.sleep(1) 
        self.driver.find_elements(*self.kpi_name)[1].send_keys(name)   
        time.sleep(1) 
        self.driver.find_elements(*self.drop_down)[0].click()   
        time.sleep(1) 
        options = self.driver.find_elements(*self.options)
        for option in options:
            try:
             if(job_title in option.text):
                option.click()
                break
            except StaleElementReferenceException:
               time.sleep(1)
        self.driver.find_elements(*self.button)[1].click()#save button
        time.sleep(3)  
        
    def activate_review(self,employee,supervisor,start_date,end_date,due_date):
        self.driver.find_elements(*self.tab_item)[1].click()
        time.sleep(1) 
        self.driver.find_element(*self.manage_reviews).click()
        time.sleep(1) 
        self.driver.find_elements(*self.button)[2].click() #add button 
        time.sleep(1) 
        self.driver.find_elements(*self.name_fields)[0].send_keys(employee)
        self.driver.find_element(*self.option).click()
        time.sleep(1)
        self.driver.find_elements(*self.name_fields)[1].send_keys(supervisor)
        self.driver.find_element(*self.option).click()
        time.sleep(1)
        self.driver.find_elements(*self.date_inputs)[1].send_keys(start_date)
        time.sleep(1)
        self.driver.find_elements(*self.date_inputs)[2].send_keys(end_date)
        time.sleep(1)
        self.driver.find_elements(*self.date_inputs)[3].send_keys(due_date)
        time.sleep(1)
        self.driver.find_elements(*self.button)[2].click()
        time.sleep(1)
        
        
        
        
        
    def verify_KPI(self, kpi_name):
        assert kpi_name in self.driver.page_source, f"{kpi_name} was not added!"
