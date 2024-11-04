import requests
import random
class TestData:
    
    API_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/job-titles?limit=50&offset=0&sortField=jt.jobTitleName&sortOrder=ASC"
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"
    EMPLOYEE_FIRST_NAME = "EmployeeFirstName"+str(random.randrange(1,1000))
    EMPLOYEE_LAST_NAME = "LastName"
    SUPERVISOR_FIRST_NAME="SupervisorFirstName"+str(random.randrange(1,1000))
    SUPERVISOR_LAST_NAME = "LastName"
    EMPLOYEE_ID = "EID"+str(random.randrange(1,100000))
    SUPERVISOR_ID = "EID"+str(random.randrange(1,100000))
    PHOTO_PATH = r"C:\Users\MAbuAlrob\Desktop\test.png"
    LEAVE_TYPE = "CAN - FMLA"
    FROM_DATE = "2024-10-10"
    TO_DATE = "2024-11-10"
    PARTIAL_DAYS = "All Days"
    START_DAY = "Half Day - Morning"
    LEAVE_COMMENT = "Personal reasons"
    REVIEW_COMMENT = "Annual review"
    DRIVER_PATH=r"C:\Users\MAbuAlrob\Desktop\chromedriver.exe"
    FILE_PATH =r'C:\Users\MAbuAlrob\Desktop\JobSpec.txt'
    description="just for testing"
    job_title = "Job Title"+str(random.randrange(1,1000))
    note = "just a note for testing"
    reporting_method="Direct"
    kpi_name="New KPI"
    START_DATE = "2024-10-1"
    END_DATE= "2024-10-15"
    DUE_DATE = "2024-10-30"
