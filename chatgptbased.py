import openai
import requests
from bs4 import BeautifulSoup

def search_stackoverflow(question):
    # Modify the question to fit the URL format
    search_query = "+".join(question.split())
    url = f"https://stackoverflow.com/search?q={search_query}"
    
    # Send GET request to Stack Overflow search page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all search result links
        search_results = soup.find_all('div', class_='question-summary search-result')
        
        # Print out the HTML content of the search results page
        # print(response.text)
        
        # Iterate through the search results to find the links to top 10 questions
        question_links = []
        for result in search_results[:10]:
            link = result.find('a', class_='question-hyperlink')
            if link:
                question_links.append("https://stackoverflow.com" + link['href'])
        
        # Print out the URLs of the question links
        print("Question links:", question_links)
        
        # Scrape top 10 answers from each question link
        top_answers = []
        for link in question_links:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                answers = soup.find_all('div', class_='answercell')
                for answer in answers:
                    top_answers.append(answer.find('div', class_='answercell').text.strip())
        
        return top_answers
    else:
        print("Failed to retrieve search results from Stack Overflow")
        return None

def summarize_answers(qn, answers):
    openai.api_key = 'PUT YOUR OPENAI API KEY HERE'  # Replace 'your_openai_api_key' with your actual OpenAI API key
    
    # Join the answers into a single text for summarization
    text = qn + "\n".join(answers)
    
    # Use ChatGPT to summarize the text
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    # Extract and return the summarized answer
    summary = response.choices[0].text.strip()
    return summary

if __name__ == "__main__":
    question = input("Enter your question: ")
    answers = search_stackoverflow(question)
    if answers:
        print("Summarizing the top answers...")
        summary = summarize_answers(question, answers)
        print("Summarized answer:", summary)
    else:
        print("No answers found for the given question.")
