data = {
    "candidates": [
        {
            "content": {
                "parts": [
                    {"text": "The review is positive."}
                ],
                "role": "model"
            },
            "finishReason": "STOP"
        }
    ],
    "usageMetadata": {"totalTokenCount": 25}
}

from google import genai

client = genai.Client()

question = input("Ask the AI:")

response = client.models.generate_content(
    model = "gemini-3.5-flash-lite",
    contents = question
)

print(response.text)