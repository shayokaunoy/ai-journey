# shop = {
#     "name": "City Mart",
#     "products": [
#         {"item": "pen", "price": 10},
#         {"item": "book", "price": 500}
#     ]
# }

# def total_price(shop, limit):
#     total = 0

#     for product in shop["products"]:
#         if product["price"] > limit:
#             total = total + product["price"]
#     return total

# shop["products"].append({"item": "bag", "price": 300})

# print(total_price(shop, 100))


reply = {
    "candidates": [
        {
            "content": {
                "parts": [
                    {"text": "Hello!"}
                ]
            }
        }
    ]
}

print(reply["candidates"][0]["content"]["parts"][0]["text"])















