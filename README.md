# QA Automation Assessment Project

This repository contains an automation testing framework designed for an interview assessment. 

**Please note:** The primary objective of this project was not to develop the target applications (`assessment_cli.py` and `assessment_ui.py`), but to create a comprehensive and robust test suite to validate them.

---

## Prerequisites

Before running the applications or the test suite, ensure your environment meets the following requirements.

### 1. Python
Python must be installed on your system. 
* Check your version: `python --version` or `python3 --version`
* If not installed, download it from the [official Python website](https://python.org).

### 2. Dependencies
Install all required Python packages using `pip`. Run the following command in your terminal:
```bash
pip install -r requirements.txt
```

### 3. Playwright
Install all required Playwright. Run the following command in your terminal:
```bash
playwright install --with-deps
```

### 3. Docker & Docker Compose (Required for UI Application)
To run and test the UI application (`assessment_ui.py`), you must have Docker and Docker Compose installed.

* **Windows:**
  1. Download and install [Docker Desktop for Windows](https://docker.com).
  2. Ensure WSL 2 (Windows Subsystem for Linux) is enabled during installation.
  3. Docker Compose comes bundled automatically with Docker Desktop.

* **Linux (Ubuntu/Debian example):**
  1. Update packages: `sudo apt-get update`
  2. Install Docker: `sudo apt-get install docker.io`
  3. Install Docker Compose: `sudo apt-get install docker-compose-v2`
  4. Start the service: `sudo systemctl start docker`

---

## Setting Up the UI Application

Before running the tests against the UI application (`assessment_ui.py`), you need to build and start its environment. 

Run the following command in the root directory of the project to build and launch the application in detached mode (in the background):

```bash
docker-compose up -d
```

---

## Running the Tests

All tests are located in the `Tests` directory. You must navigate into this folder before executing any test commands.

```bash
cd Tests
```

### Standard Test Execution
To run the test suite with verbose output and standard stdout printing enabled, use:
```bash
pytest -vv -s
```

### Test Execution with Allure Reporting (Optional)
If you want to generate a detailed visual test report using Allure, follow these steps:

1. **Prerequisite:** Ensure Allure Commandline is installed on your system ([Installation Guide](https://allurereport.org)).
2. Execute the tests while specifying the results directory:
   ```bash
   pytest -vv -s --alluredir=test_report
   ```
3. To generate and view the interactive HTML report in your browser after the execution completes, run:
   ```bash
   allure serve test_report
   ```

---

## Project Structure

* `App/assessment_cli.py` - The target Command Line Interface application.
* `App/assessment_ui.py` - The target User Interface application (requires Docker container environment).
* `requirements.txt` - Python dependencies file.
* `Tests/` - Directory containing the automated test cases and configuration.
