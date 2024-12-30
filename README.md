# ElasticAI
1. Importing libraries 
	a. webdriver --> Enables to control the chrome browser
	b. by --> a mechanism for locating the elements on the webpage like id, classname or CSS selector)
	c. service --> Path specifies the path to the Chromedriver.exe
	d. options --> Configures the chrome browser settings

2. Configuring WebDriver:  get_driver() will initialise the webDriver 
	a. Headless --> For testing non - GUI environments. 
	b. service class will help in initialising the chromeDriver Path (this is the path 	in my PC)
	c. Driver object helps to interact with the browser. 

3. get_driver() function shall initialise the WebDriver

4. driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo") opens the webpage 

5. Interaction with the search box : search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']") --> finds the search input box using the CSS selector 
search_box.clear()  --> Clears any pre-filled text
search_box.send_keys("New York") --> Enters "New York" into the search box

6. Validating the search results: 
table_rows = driver.find_elements(By.CSS_SELECTOR, "table#example tbody tr") --> All rows will be found using CSS selector. 
visible_rows = [row for row in table_rows if row.is_displayed()] --> filters the rows 

7. Print and Assert:
print(f"Count of visible rows: {len(visible_rows)}") --> prints the number of visible rows matching our query. 
assert len(visible_rows) == 5, f"Expected 5 rows, but found {len(visible_rows)}" --> asserts that there are 5 rows. but, if not then it raises an Assertion error with a message (for eg: Expected 5 rows, but found 4 rows)

8. Error handling 
print("Test Passed: Search functionality works as expected!") --> if test passess
except AssertionError as e:
    print(f"Test Failed: {e}")   --> if test fails. this bblock catches the assertionerror and prints the error message. 

9. Closing the browser --> finally:
   			   driver.quit()

Regardless of success or failure of the test cases, the browser should be closed. 

10.test_search_functionality() --> Invokes the function to perform the test. 



