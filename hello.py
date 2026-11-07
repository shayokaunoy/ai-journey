# import os
# import json
# import requests

# key = os.environ["GEMINI_API_KEY"]
# url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"
# headers = {"x-goog-api-key": key}
# body = {"contents": [{"parts": [{"text": "Say hello in one short line"}]}]}   # FIXED: content -> contents (শেষে s)

# reply = requests.post(url, headers=headers, json=body)
# print(reply.status_code)
# data = json.loads(reply.text)

# print(data["candidates"][0]["content"]["parts"][0]["text"])   # FIXED: test -> text



shop = {
    "name": "City Mart",
    "products": [
        {"item": "pen", "price": 10},
        {"item": "book", "price": 50},
        {"item": "bag", "price": 300}
    ]
}

total = 0

for products in shop["products"]:
    total = total + products["price"]

print("Total Price:", total)

# print(shop["products"][2]["price"] + shop["products"][0]["price"])