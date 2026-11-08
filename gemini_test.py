from google import genai

client = genai.Client()

def ask_gemini(questions):
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = questions
    )
    return response.text
reviews = ["The pen is very good.", "The bag broke in one day.", "Nice book, I liked it.", "Very bad quality.", "Worth the price."]

# step 1: make count = 0 before the loop
# step 2: loop over reviews
# step 3: ask Gemini inside the loop and keep the reply in answer
# step 4: if answer is "Positive", add 1 to count
# step 5: after the loop, print the count

count = 0
for review in reviews:
    answer = ask_gemini("Is this review positive or negative? Answer with one word only. Review:" + review)
    if answer == "Positive":
        count = count + 1
print(count)