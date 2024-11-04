import requests
import os
import logging
import cv2  
import numpy as np
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
from data.test_data import TestData
from pages.job_titles_page import JobTitlesPage
from pages.performance_page import PerformancePage
import threading
import time

# Setup logging
logging.basicConfig(filename="test_logs.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Screen Capture Settings
FRAME_RATE = 20  # Higher frame rate for smoother playback
VIDEO_CODEC = cv2.VideoWriter_fourcc(*"mp4v")
VIDEO_RESOLUTION = (1280, 720)  # Higher resolution for better quality

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

def log_message(message):
    logging.info(message)

# Start recording frames for video
def start_video_recording(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_path = f"videos/{test_name}_{timestamp}.mp4"
    video_writer = cv2.VideoWriter(video_path, VIDEO_CODEC, FRAME_RATE, VIDEO_RESOLUTION)
    return video_writer, video_path
    
# Capture a single frame
def capture_frame(driver, video_writer):
    png = driver.get_screenshot_as_png()
    img_np = np.frombuffer(png, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    resized_img = cv2.resize(img, VIDEO_RESOLUTION)  
    video_writer.write(resized_img)

def continuous_capture(driver, video_writer, stop_event):
    """Continuously capture frames during test execution."""
    while not stop_event.is_set():
        capture_frame(driver, video_writer)
        time.sleep(1 / FRAME_RATE)  # Delay for smoother video

def main():
    service = Service(executable_path=TestData.DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    # Initialize variables
    error_occurred = False
    stop_event = threading.Event()
    video_writer = None

    try:
        # Start video recording
        video_writer, video_path = start_video_recording(driver, "test_execution")

        # Start continuous frame capture
        capture_thread = threading.Thread(target=continuous_capture, args=(driver, video_writer, stop_event))
        capture_thread.daemon = True
        capture_thread.start()

        # Login Test
        driver.get(TestData.URL)
        
        try:
            login_page = LoginPage(driver)
            login_page.enter_username(TestData.USERNAME)
            login_page.enter_password(TestData.PASSWORD)
            login_page.click_login()
        except Exception as e:
            log_message(f"Error during login: {str(e).splitlines()[0]}")
            take_screenshot(driver, "login_failure")
            error_occurred = True  

        # Add a job title
        #'''
        if not error_occurred:  # Only proceed if no error occurred
            try:
                job_titles_page = JobTitlesPage(driver)
                job_titles_page.add_job_title(TestData.job_title, TestData.description, TestData.FILE_PATH, TestData.note)
                job_titles_page.verify_job_title_added(TestData.job_title)
            except Exception as e:
                log_message(f"Error adding job title: {str(e).splitlines()[0]}")
                take_screenshot(driver, "job_title_failure")
                error_occurred = True  

        # Add Employee 
        
        if not error_occurred: 
            try:
                employee_page = EmployeePage(driver)
                employee_page.add_supervisor(TestData.SUPERVISOR_FIRST_NAME, TestData.SUPERVISOR_LAST_NAME, TestData.SUPERVISOR_ID, TestData.PHOTO_PATH)
                employee_page.verify_employee_added(TestData.SUPERVISOR_ID)
                employee_page.add_employee(TestData.EMPLOYEE_FIRST_NAME, TestData.EMPLOYEE_LAST_NAME, TestData.EMPLOYEE_ID, TestData.PHOTO_PATH)
            except NoSuchElementException as e:
                log_message(f"Error adding employee: {str(e).splitlines()[0]}")
                take_screenshot(driver, "employee_failure")
                error_occurred = True  
            except Exception as e:
                log_message(f"Unexpected error during employee addition: {str(e).splitlines()[0]}")
                take_screenshot(driver, "unexpected_employee_failure")
                error_occurred = True #''' 
                
        #Add KPI
        if not error_occurred:  
            try:
                performance_page = PerformancePage(driver)
                performance_page.add_kpi(TestData.kpi_name,TestData.job_title)
            except NoSuchElementException as e:
                log_message(f"Error adding KPI: {str(e).splitlines()[0]}")
                take_screenshot(driver, "KPI_failure")
                error_occurred = True  
            except Exception as e:
                log_message(f"Unexpected error during kPI addition: {str(e).splitlines()[0]}")
                take_screenshot(driver, "unexpected_KPI_failure")
                error_occurred = True  
                
        #Activate Review 
        if not error_occurred:  
            try:
                performance_page = PerformancePage(driver)
                performance_page.activate_review(TestData.EMPLOYEE_FIRST_NAME,TestData.SUPERVISOR_FIRST_NAME,TestData.START_DATE,TestData.END_DATE,TestData.DUE_DATE)
            except NoSuchElementException as e:
                log_message(f"Error adding KPI: {str(e).splitlines()[0]}")
                take_screenshot(driver, "KPI_failure")
                error_occurred = True  
            except Exception as e:
                log_message(f"Unexpected error during kPI addition: {str(e).splitlines()[0]}")
                take_screenshot(driver, "unexpected_KPI_failure")
                error_occurred = True

    except Exception as e:
        log_message(f"Unexpected error: {str(e).splitlines()[0]}")
        take_screenshot(driver, "unexpected_error")
        error_occurred = True  
        #--

    finally:
        # Delay before stopping video recording to capture any aftermath of the error
        if error_occurred:
            time.sleep(10)  # Capture for 5 more seconds after error
        stop_event.set()  # Signal to stop video capture
        capture_thread.join()  # Wait for capture thread to finish
        if video_writer:
            video_writer.release()  # Save the video
        driver.quit()  # Ensure the driver quits properly
        log_message("Driver quit.")

if __name__ == "__main__":
    main()
