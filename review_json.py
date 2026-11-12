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

question = 'Review: "Great quality, fast delivery". Answer only in JSON like {"label": "positive"} or {"label": "negative"}'


# fenced = '```json\n{"label": "positive"}\n```'
# print(get_label(fenced))

answer = '{"label": "negative"}'
print(answer)
print(get_label(answer))


