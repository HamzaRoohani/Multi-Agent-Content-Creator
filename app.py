import gradio as gr
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

history = []

def chat(user_message, history_gradio):
    history.append({"role": "user", "parts": [{"text": user_message}]})

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )
    ai_response = response.text
    history.append({"role": "model", "parts": [{"text": ai_response}]})

    return ai_response

app = gr.ChatInterface(
    fn=chat,
    title="AI Chatbot",
    description="A chatbot with memory powered by Gemini 2.5 Flash"
    )

app.launch()