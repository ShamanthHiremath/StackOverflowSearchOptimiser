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
    # https://stackoverflow.com/search?q=+how+to+upgrade+python+version
    url = f"https://stackoverflow.com/search?q={quote(question)}"
    
    fetchAndSaveAsHTML(url, "data/stackOverflowQnScrape.html")
    
    # Send GET request to Stack Overflow search page
    # response = requests.get(url)
    response = readHTMLFile("data/stackOverflowQnScrape.html")
    
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        
        # Find all search result links
        search_results = soup.find_all('a', class_='s-link')
        
        # Print out the HTML content of the search results page
        # print(response.text)
        
        # Iterate through the search results to find the links to top 10 questions
        # Go through all the question_links and find the one containing the qn_ as its string store it in question_link and store answers in top_answers
        question_mapping = {}
        top_questions = []

        for link in search_results:
            if link:
                # Extract the question string and URL from the search result
                question_string = link.text.strip()
                question_url = "https://stackoverflow.com" + link['href']
                question_mapping[question_string] = question_url
                top_questions.append(question_string)

        print(top_questions)
        print(question_mapping)        
        # Find the most relevant question asked by the user and store it in qn_  
        # most_similar_qn_ =  chatGPTSummary.mostSimilarQn(question, top_10_questions)
        # most_similar_qn_link = question_mapping[most_similar_qn_]
        if(len(top_questions) != 0):
            
            most_similar_qn_ =  top_questions[0]
            most_similar_qn_link = question_mapping[most_similar_qn_]
        else:
            print("EMPTY")   
        
        return 
        
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
    
    
# def main():
    # Main functionality of your script
    
# if __name__ == "__main__":
    # main()
    
search_input = input("ENTER THE QUESTION TO BE SEARCHED IN STACKOVERFLOW: ")
answers = search_stackoverflow(search_input)

    
    



