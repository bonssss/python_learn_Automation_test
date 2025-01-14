import datetime
import os
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Get the current date in the desired format
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Define the base directory where reports will be saved
    base_dir = r"C:\Users\bons\Documents\Website_projects\python learn\netryde"

    # Create the 'Reports' directory within the base directory
    reports_dir = os.path.join(base_dir, 'Report')
    os.makedirs(reports_dir, exist_ok=True)

    # Retrieve the test file name without extension
    if config.args:
        test_file_name = os.path.splitext(os.path.basename(config.args[0]))[0]
    else:
        test_file_name = 'report'

    # Construct the HTML report filename
    report_filename = f"{test_file_name}_{current_date}.html"

    # Set the HTML report path
    config.option.htmlpath = os.path.join(reports_dir, report_filename)
