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


def count_positive(reviews):
    count = 0

    for review in reviews:
        question = "Is this review positive or negative? Answer with one word: " + review
        answer = ask_gemini(question)

        if answer == "Positive":
            count = count + 1
    return count

def positive_reviews(reviews):
    positives = []

    for review in reviews:
        question = "Is this review positive or negative? Answer with one word: " + review
        answer = ask_gemini(question)

        if answer == "Positive":
            positives.append(review)
    return positives

def save_positive(reviews, filename):
    count = 0
    with open(filename, "w") as f:
        for review in reviews:
            question = "Is this review positive or negative? Answer with one word: " + review
            answer = ask_gemini(question)
            if answer == "Positive":
                f.write(review + "\n")
                count = count + 1
    return count


positives = positive_reviews(reviews)
with open(r"E:\ai-journey\positives.txt", "w") as f:
    for item in positives:
        f.write(item + "\n")
with open(r"E:\ai-journey\positives.txt", "r") as f:
    print(f.read(), end="")

saved = save_positive(reviews, r"E:\ai-journey\positives2.txt")
print("Saved:", saved)


    








