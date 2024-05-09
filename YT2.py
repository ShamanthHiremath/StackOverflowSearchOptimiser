import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrapeNPrint():
    
    url = "https://stackoverflow.com/questions"
    
    # Send GET request to Stack Overflow search page
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # print(soup.prettify)
    
    qn_summary = {
            "ques" : [],
            
        }
    
    # qn1 = questions[0].select('.question-hyperlink')
    questions = soup.select(".question-summary")
    
    for qn in questions:
        qn_text = qn.select_one('.question-hyperlink').getText()
        vote_text = qn.select_one('.vote-count-post').getText()
        views_text = qn.select_one('.views').attrs['title']
        print("QN: ", qn_text)
        print("Vote Count: ", vote_text)
        print("Views: ", views_text)
        qn_summary["ques"].append({
            "question": qn_text,
            "votes": vote_text,
            "views": views_text
        })
        
    json_data = json.dumps(qn_summary)
    
    print(json_data)
        
scrapeNPrint()




