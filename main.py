import webScrape
from chatGPTSummary import summarize_answers

search_input = input("ENTER THE QUESTION TO BE SEARCHED IN STACKOVERFLOW: ")
answers = webScrape.search_stackoverflow(search_input)

if answers:
    summary = summarize_answers(search_input, answers)
    print("Summarized Answer:", summary)
else:
    print("No answers found for the given question.")
