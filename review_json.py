import json
from ask_gemini import ask_gemini

def get_label(text):

    data = json.loads(text)
    return data["label"]

texts = [
    '{"label": "positive", "reason": "good quality"}',
    '{"label": "negative", "reason": "late delivery"}',
    '{"label": "positive", "reason": "fast delivery"}',
    '{"label": "positive", "reason": "nice price"}',
]
def count_positive(texts):

    count = 0
    for text in texts:
        label = get_label(text)
        if label == "positive":
            count = count + 1
    return count

# print(count_positive(texts))

# question = 'Review: "Great quality, fast delivery". Answer only in JSON like {"label": "positive"} or {"label": "negative"}'


# # # fenced = '```json\n{"label": "positive"}\n```'
# # print(get_label(fenced))

# answer = ask_gemini(question)

# label = get_label(answer)
# print(label)
def safe_label(text):
    # text = text.replace("```json", "")
    # text = text.replace("```", "")
    try:
        data = json.loads(text)
        return data["label"]
    except json.JSONDecodeError:
        return "unknown"


clean = '{"label": "negative"}'
messy = 'Sure! Here is the answer: {"label": "positive"}'

# print(safe_label(clean))
# print(safe_label(messy))
# print("Done")


reviews = [
    "Great quality, fast delivery",
    "The product broke after two days",
    "Very happy with the price",
    "Late delivery and rude support",
]

def label_all(reviews):
    result = []

    for review in reviews:

        question = 'Review: "' + review + '". Answer only in JSON like {"label": "positive"} or {"label": "negative"}'

        answer = ask_gemini(question)
        # print(answer) 

        label = safe_label(answer)

        result.append(label)

    return result

print(label_all(reviews))