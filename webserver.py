import logging
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver_path = "/path/to/chromedriver"  # Replace with the actual path to chromedriver executable

# Set up logging
logging.basicConfig(level=logging.ERROR)

# Open the browser
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

@app.route('/discord', methods=['GET'])
def discord():
    return "chrisstheg"

@app.route('/code', methods=['GET'])
def perform_actions():
    email = request.args.get('email')
    if not email:
        return 'Bad Request', 400

    try:
        # Navigate to the login page
        driver.get('https://login.live.com')
        time.sleep(2)  # Wait for 2 seconds

        # Enter the email and click 'next'
        driver.find_element(By.NAME, 'loginfmt').send_keys(email)
        driver.find_element(By.ID, 'idSIButton9').click()
        time.sleep(2)  # Wait for 2 seconds
        try:
            # Click 'Email code'
            driver.find_element(By.LINK_TEXT, 'Email code').click()
            time.sleep(2)  # Wait for 2 seconds
            return "Success [code]: Email code clicked successfully"
        except:
            return 'Error [code]: No Email code found', 204
    except Exception as e:
        logging.error(str(e))
        return 'An error occurred while performing actions', 500

@app.route('/')
def online():
    return 'OTP Requester'

if __name__ == '__main__':
    app.run(port=80)
