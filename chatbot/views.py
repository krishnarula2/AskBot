import os
from dotenv import load_dotenv
from django.http import JsonResponse
from django.shortcuts import render
from askbot_project.settings import BASE_DIR

# Load environment variables from .env
dotenv_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Get Together.ai API key
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Optional debug print
if TOGETHER_API_KEY:
    print("✅ TOGETHER_API_KEY loaded.")
else:
    print("❌ TOGETHER_API_KEY not found. Check your .env file.")

# Initialize Together.ai client
from openai import OpenAI

client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1"
)

# Route for serving the chatbot UI
def chat_ui(request):
    return render(request, "chatbot.html")

# Route for handling user messages
def chat_with_bot(request):
    user_input = request.GET.get("message", "")

    try:
        # Build the request to Together.ai (e.g., using Mistral model)
        response = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": "You are AskBot, a helpful assistant for small business users."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150,
        )

        reply = response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ ERROR in chat_with_bot():", e)
        reply = "Bot: Failed to get response from server."

    return JsonResponse({"response": reply})
