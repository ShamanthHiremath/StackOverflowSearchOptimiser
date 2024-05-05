import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote
import chatGPTSummary

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetchAndSaveAsHTML(url, path):
    # Increase timeout value (in seconds)
    timeout = 10  # Adjust as needed
    r = requests.get(url, headers=headers, timeout=timeout)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
        
def readHTMLFile(filename):
    with open(filename, "r") as f:
        html_doc = f.read()
    return html_doc

def search_stackoverflow(question):
    encoded_input = quote(question)
    # Modify the question to fit the URL format
    search_query = "+".join(question.split())
    url = f"https://stackoverflow.com/search?q={search_query}"
    
    fetchAndSaveAsHTML(url, "data/stackOverflowQnScrape.html")
    
    # Send GET request to Stack Overflow search page
    # response = requests.get(url)
    response = readHTMLFile("data/stackOverflowQnScrape.html")
    
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        
        # Find all search result links
        search_results = soup.find_all('div', class_='question-summary search-result')
        
        # Print out the HTML content of the search results page
        # print(response.text)
        
        # Iterate through the search results to find the links to top 10 questions
        # Go through all the question_links and find the one containing the qn_ as its string store it in question_link and store answers in top_answers
        question_mapping = {}
        top_10_questions = []

        for result in search_results[:10]:
            link = result.find('a', class_='question-hyperlink')
            if link:
                # Extract the question string and URL from the search result
                question_string = link.text.strip()
                question_url = "https://stackoverflow.com" + link['href']
                question_mapping[question_string] = question_url
                top_10_questions.append(question_string)

                
        # Find the most relevant question asked by the user and store it in qn_  
        most_similar_qn_ =  chatGPTSummary.mostSimilarQn(question, top_10_questions)
        most_similar_qn_link = question_mapping[most_similar_qn_]        
        
        # Print out the URLs of the question links
        # print("Question links:", question_links)
        
        # Scrape top 10 answers from just the most_similar_qn_link 
        top_answers = []
        
        response = requests.get(most_similar_qn_link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            answers = soup.find_all('div', class_='answercell')
            for answer in answers:
                top_answers.append(answer.find('div', class_='answercell').text.strip())
    
        return top_answers
    else:
        print("Failed to retrieve search results from Stack Overflow")
        return None


