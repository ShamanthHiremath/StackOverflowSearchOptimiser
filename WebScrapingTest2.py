import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def search_stackoverflow(question):
    # Modify the question to fit the URL format
    search_query = "+".join(question.split())
    url = f"https://stackoverflow.com/search?q={search_query}"
    
    print("\n\n", url, "\n\n")
    
    # Send GET request to Stack Overflow search page
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all search result links
         # Find the mainbar section
        mainbar = soup.find('div', id='mainbar')
        # if mainbar:
            # Find all <a> elements with class 's-link' within the mainbar section
        search_results = mainbar.find_all('a', class_='s-link')
        
        # Iterate through the search results to find the links to top questions
        question_mapping = {}
        top_questions = []

        for link in search_results:
            if link:
                # Extract the question string and URL from the search result
                question_string = link.text.strip()
                question_url = "https://stackoverflow.com" + link['href']
                question_mapping[question_string] = question_url
                top_questions.append(question_string)
                
        print("QUESTION LIST IS:  \n")
        print(top_questions)
        print("\nQUESTION LIST IS:  \n")
        print(question_mapping)

search_input = input("ENTER THE QUESTION TO BE SEARCHED IN STACKOVERFLOW: ")
search_stackoverflow(search_input)