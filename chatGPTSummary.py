import openai

openai.api_key = 'PUT YOUR OPENAI API KEY HERE'  # Replace 'your_openai_api_key' with your actual OpenAI API key

def mostSimilarQn(user_qn, qn_list):
    # Initialize variables to store the most similar question link and its similarity score
    most_similar_qn = None
    max_similarity_score = -1
    
    # Iterate through the list of question links
    for qn in qn_list:
        # Compute the similarity score between the user question and the current question link
        similarity_score = compute_similarity(user_qn, qn)
        
        # Update the most similar link if the current link has a higher similarity score
        if similarity_score > max_similarity_score:
            max_similarity_score = similarity_score
            most_similar_qn = qn
    
    return most_similar_qn

def compute_similarity(qn1, qn2):
    # Use OpenAI's similarity model to compute the similarity between two questions
    # openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Compute the similarity between the following two questions:\n\n1. {qn1}\n\n2. {qn2}\n",
        max_tokens=50,
        temperature=0.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    
    # Extract and return the similarity score from the response
    similarity_score = response.choices[0].score
    return similarity_score


def summarize_answers(qn, answers):
    
    # Join the questions and answers into a single text for summarization
    prompt = f"""
    Below are the question and answers provided by users in response to a Stack Overflow query regarding '{qn}':
    
    Question:
    {qn}
    
    Answers:
    {answers}
    
    Now, please provide the most summarized optimal answer that resolves the question.
    """
    print(prompt)
    
    # Use ChatGPT to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,  # Changed from 'text' to 'prompt'
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    # Extract and return the summarized answer
    summary = response.choices[0].text.strip()
    return summary