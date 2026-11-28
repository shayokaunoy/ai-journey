import json
with open(r"E:\ai-journey\labels.json", "r") as f:
    text = f.read()
labels = json.loads(text)
for item in labels:
    print(item)