import os
import json
import requests

def ask_gemini(questions):
    key = os.environ["GEMINI_API_KEY"]
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
reviews = [
    "Great phone, battery lasts two days",
    "The shoes broke after one week",
    "Fast delivery and nice packing",
    "Screen is dull and the price is too high",
    "Very comfortable chair, I love it",
]

def label_reviews(reviews):
    for review in reviews:
        question = "Is this postivie or negative write it with one word" + review
        answer = ask_gemini(question)

print(answer)