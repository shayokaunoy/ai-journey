import os
import json
import requests

def ask_gemini(questions):
    key = os.environ["Gemini_API_KEY"]
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"
    # url = "https://gggg-WTF-HAHAHAHA"
    headers = {"x-goog-api-key": key}
    body = {"contents": [{"parts": [{"text": questions}]}]}

    try:
        response = requests.post(url, headers = headers, json = body)

    except Exception as e:
        print(e)
        return "Call Failed"
    
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Call Failed"

# reviews = [
#     "Very good pen, writes smoothly",
#     "The bag broke in two days",
#     "Nice book, fast delivery",
#     "Too expensive and the quality is bad",
#     "I love this shop"
# ]

with open(r"E:\ai-journey\reviews.json", "r") as f:
    text = f.read()
reviews = json.loads(text)

def count_result(reviews):
    positive = 0
    failed = 0
    for review in reviews:
        question = "Is this review positive or negative? Answer in one word: " + review
        answer = ask_gemini(question)
        if answer == "Positive":
            positive = positive + 1
        elif answer == "Call Failed":
            failed = failed + 1
    
    return positive, failed


def label_reviews(reviews):
    result = []
    for review in reviews:
        question = "Is this review positive or negative? Answer in one word: " + review
        answer = ask_gemini(question)
        result.append({"review": review, "label": answer})
    return result




labeled = label_reviews(reviews)
print(labeled)


        
positive, failed = count_result(reviews)
print("Positive:", positive)
print("Failed:", failed)      
