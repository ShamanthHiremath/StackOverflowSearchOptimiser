import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_stackoverflow(question):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()  # Update this with the path to your WebDriver

    # Navigate to the Stack Overflow search page
    driver.get("https://stackoverflow.com")

    # Find the search input element
    search_input = driver.find_element_by_name("q")

    # Enter the question into the search input
    search_input.send_keys(question)

    # Submit the search query
    search_input.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

    # Find all search result links
    search_results = driver.find_elements_by_css_selector(".search-results .js-search-results .question-hyperlink")

    # Extract the question string and URL from the search results
    top_questions = [result.text for result in search_results]
    question_mapping = {result.text: result.get_attribute("href") for result in search_results}

    print("QUESTION LIST IS:  \n")
    print(top_questions)
    print("\nQUESTION LIST IS:  \n")
    print(question_mapping)

    # Close the WebDriver
    driver.quit()

search_input = input("ENTER THE QUESTION TO BE SEARCHED IN STACKOVERFLOW: ")
search_stackoverflow(search_input)
