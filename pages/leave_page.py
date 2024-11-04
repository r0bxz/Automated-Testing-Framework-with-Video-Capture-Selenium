from selenium.webdriver.common.by import By

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.leave_type_dropdown = (By.NAME, "leaveType")
        self.from_date_field = (By.NAME, "fromDate")
        self.to_date_field = (By.NAME, "toDate")
        self.partial_days_dropdown = (By.NAME, "partialDays")
        self.start_day_dropdown = (By.NAME, "startDay")
        self.comment_field = (By.NAME, "comments")
        self.apply_button = (By.CSS_SELECTOR, ".oxd-button--secondary")

    def apply_leave(self, leave_type, from_date, to_date, partial_days, start_day, comment):
        self.driver.find_element(*self.leave_type_dropdown).send_keys(leave_type)
        self.driver.find_element(*self.from_date_field).send_keys(from_date)
        self.driver.find_element(*self.to_date_field).send_keys(to_date)
        self.driver.find_element(*self.partial_days_dropdown).send_keys(partial_days)
        self.driver.find_element(*self.start_day_dropdown).send_keys(start_day)
        self.driver.find_element(*self.comment_field).send_keys(comment)
        self.driver.find_element(*self.apply_button).click()

    def verify_leave_applied(self, from_date, to_date):
        assert f"{from_date} to {to_date}" in self.driver.page_source, "Leave not applied!"
