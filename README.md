# Selenium Python Automation Framework
Project Overview
This project is a Selenium Python Automation Framework designed for end-to-end UI automation using Python. It follows the Page Object Model (POM) design pattern and uses PyTest for test execution. HTML reports are generated for test results.

⚙️ Tech Stack
•	- Python 3
•	- Selenium WebDriver
•	- PyTest
•	- Page Object Model (POM)
•	- pytest-html (for reports)

🌟 Framework Highlights
•	- Modular design using Page Object Model
•	- PyTest-based execution with reusable fixtures
•	- Explicit waits for reliable element interaction
•	- HTML reporting for test results
•	- Easy-to-extend structure for new test cases

📁 Project Structure
Folder/File	Description
pages/	Contains BasePage and LoginPage classes
tests/	PyTest test scripts
reports/	HTML reports generated after test execution
requirements.txt	Python dependencies

🧩 Pages
BasePage
•	- open(url) – Opens a URL
•	- find(locator) – Waits for element presence
•	- click(locator) – Waits and clicks element
•	- type(locator, text) – Clears and types text
•	- text_of(locator) – Gets trimmed text
•	- is_visible(locator) – Checks visibility
LoginPage
•	- load(base_url) – Opens login page
•	- login(username, password) – Performs login

🚀 How to Run Tests
1. Install dependencies
pip install -r requirements.txt

3. Run PyTest tests
pytest

5. View HTML Report
After running tests, open 'report.html' in the 'reports/' folder.
📊 Sample Report
•	- Generated using pytest-html
•	- Shows test status: Passed, Failed, Skipped
•	- Includes logs and media (screenshots)

👩‍💻 Author
Shaik Mahammad Rajak
QA Automation Tester
