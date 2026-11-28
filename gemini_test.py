from google import genai

client = genai.Client()

def ask_gemini(questions):
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = questions
    )
    return response.text

def count_positive(reviews):
    count = 0
    for review in reviews:
        answer = ask_gemini("Is this review positive or negative? Answer with one word only. Review: " + review)
        if answer == "Positive":
            count = count + 1
    return count

test_reviews = ["The pen is very good.", "The bag broke in one day.", "Nice book, I liked it.", "Very bad quality.", "Worth the price."]
print(count_positive(test_reviews))