# Automated Testing Framework with Video Capture

## Overview
This project provides an automated testing framework using Selenium, with structured logging, screenshot capture, and video recording capabilities. It’s designed to handle complex web-based scenarios, making it ideal for QA engineers seeking a robust, maintainable solution.

## Features
- **Selenium-based Automated Testing**: Automates testing for web applications.
- **Page Object Model (POM)**: Separates page actions for cleaner code.
- **Error Handling with Screenshots**: Automatically captures screenshots when errors occur.
- **Continuous Video Recording**: Records tests as videos to review failures in detail.
- **Structured Logging**: Records logs of each test step and error for tracking and debugging.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Automated-Testing-Framework-with-Video-Capture.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Automated-Testing-Framework-with-Video-Capture
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Configure Test Data**: Update `data/test_data.py` with your test data.
2. **Run Tests**:
    ```bash
    python src/main.py
    ```

## Folder Structure
- `src/`: Contains all the source code and modules.
- `pages/`: Stores Page Object Model files for each page.
- `data/`: Stores test data constants.
- `videos/`: Saved test videos are stored here.
- `screenshots/`: Captured error screenshots are stored here.

## Requirements
- Python 3.x
- Selenium
- OpenCV
- NumPy

## Contributing
Feel free to fork and contribute! Open a PR for any improvements or bug fixes.
