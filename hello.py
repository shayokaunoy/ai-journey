import os
import json
import requests

key = os.environ["GEMINI_API_KEY"] # i have to ask question if this gemini api key is fixed or something madeup
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"
headers = {"x-goog-api-key": key}
body = {"contents": [{"parts": [{"text": "Say hello in one short line"}]}]}

reply = requests.post(url, headers = headers, json = body)
print(reply.status_code)
data = json.loads(reply.text)

