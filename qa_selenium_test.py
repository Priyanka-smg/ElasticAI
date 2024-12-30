from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Step 1: Configure WebDriver for Headless Chrome
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use the Service class to specify the path to the ChromeDriver
    service = Service("C:\Chromium\Driver\chromedriver.exe")  # Replace with the actual path to ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Step 2: Define the Test Function
def test_search_functionality():
    driver = get_driver()

    try:
        # Navigate to Selenium Playground Table Sort Search Demo
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

        # Locate the search box and perform search
        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_box.clear()
        search_box.send_keys("New York")

        # Validate search results
        table_rows = driver.find_elements(By.CSS_SELECTOR, "table#example tbody tr")
        visible_rows = [row for row in table_rows if row.is_displayed()]

        # Print the count of visible rows
        print(f"Count of visible rows: {len(visible_rows)}")

        # Assert there are 5 visible rows
        assert len(visible_rows) == 5, f"Expected 5 rows, but found {len(visible_rows)}"

        print("Test Passed: Search functionality works as expected!")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

# Step 3: Run the Test
test_search_functionality()
