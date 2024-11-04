from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class JobTitlesPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    ADMIN_MENU = (By.CLASS_NAME, "oxd-main-menu-item")  # Admin menu item
    JOB_MENU = (By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")  # Job menu
    JOB_TITLE_MENU = (By.CLASS_NAME, "oxd-topbar-body-nav-tab-link")  # Job Title menu
    ADD_BUTTON = (By.CLASS_NAME, "oxd-button")  # Add button for job title
    JOB_TITLE_INPUT = (By.CLASS_NAME, "oxd-input")  # Job Title input
    JOB_DESCRIPTION = (By.CLASS_NAME, "oxd-textarea")  # Job Description textarea
    FILE_INPUT = (By.CLASS_NAME, "oxd-file-input")  # File input for job spec
    NOTE_INPUT = (By.CLASS_NAME, "oxd-textarea")  # Note input
    SAVE_BUTTON = (By.CLASS_NAME, "orangehrm-left-space")  # Save button
    JOB_TITLES = (By.CLASS_NAME, "oxd-table-card")  # Job Titles in the table
    DELETE_BUTTON = (By.CLASS_NAME, "oxd-icon-button")  # Delete button icon
    CONFIRMATION_DIALOG = (By.CLASS_NAME, "orangehrm-dialog-popup")  # Confirmation dialog

    def add_job_title(self, title, description, file_path, note):
        self.driver.find_elements(*self.ADMIN_MENU)[0].click()
        time.sleep(2)
        self.driver.find_elements(*self.JOB_MENU)[1].click()
        time.sleep(2)
        self.driver.find_elements(*self.JOB_TITLE_MENU)[0].click()
        time.sleep(2)
        self.driver.find_element(*self.ADD_BUTTON).click()
        time.sleep(2)
        self.driver.find_elements(*self.JOB_TITLE_INPUT)[1].send_keys(title)
        time.sleep(2)
        self.driver.find_elements(*self.JOB_DESCRIPTION)[0].send_keys(description)
        time.sleep(2)
        self.driver.find_element(*self.FILE_INPUT).send_keys(file_path)
        time.sleep(2)
        self.driver.find_elements(*self.NOTE_INPUT)[1].send_keys(note)
        time.sleep(2)
        self.driver.find_element(*self.SAVE_BUTTON).click()
        time.sleep(2)

    def verify_job_title_added(self, title):
        job_titles = self.driver.find_elements(*self.JOB_TITLES)
        assert any(title in row.text for row in job_titles), "New job title was not added!"

    def edit_job_title(self, old_title, new_title):
        job_titles = self.driver.find_elements(*self.JOB_TITLES)
        for row in job_titles:
            if old_title in row.text:
                edit_button = row.find_element(By.CSS_SELECTOR, ".oxd-icon.bi-pencil-fill")
                edit_button.click()
                time.sleep(2)
                edited_job_title_input = self.driver.find_elements(*self.JOB_TITLE_INPUT)[1]
                edited_job_title_input.send_keys(Keys.CONTROL + "a")
                edited_job_title_input.send_keys(Keys.DELETE)
                time.sleep(2)
                edited_job_title_input.send_keys(new_title)
                time.sleep(2)
                self.driver.find_elements(By.CLASS_NAME, "oxd-radio-input")[1].click()
                time.sleep(2)
                self.driver.find_element(*self.SAVE_BUTTON).click()
                break

    def delete_job_title(self, title):
        job_titles = self.driver.find_elements(*self.JOB_TITLES)
        for row in job_titles:
            if title in row.text:
                row.find_elements(*self.DELETE_BUTTON)[0].click()
                time.sleep(2)
                confirmation_dialog = self.driver.find_element(*self.CONFIRMATION_DIALOG)
                yes_delete_button = confirmation_dialog.find_element(By.XPATH, "//button[contains(., 'Yes, Delete')]")
                yes_delete_button.click()
                time.sleep(2)
                break

    def verify_job_title_deleted(self, title):
        job_titles = self.driver.find_elements(*self.JOB_TITLES)
        assert not any(title in row.text for row in job_titles), "Job title was not deleted!"
