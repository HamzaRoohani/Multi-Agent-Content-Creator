---
title: AI Chatbot
emoji: 🏆
colorFrom: pink
colorTo: purple
sdk: gradio
sdk_version: 6.11.0
app_file: app.py
pinned: false
license: mit
short_description: AI Chatbot used to answer every user's question
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

AI Chatbot with Memory
A conversational AI chatbot powered by Google Gemini just like talking to a real assistant!

Try it for free on Hugging Face Spaces: https://huggingface.co/spaces/HamzaRoohani/AI-Chatbot
What Makes This Special?
Most basic AI apps forget everything after each message. This chatbot maintains full conversation history — so it understands context, remembers your name, and gives smarter responses as the conversation grows!

What It Does
- Maintains full conversation memory across the entire session
- Answers any question intelligently using Google Gemini 2.5 Flash
- Understands context from earlier in the conversation
- Clean and simple chat UI powered by Gradio


How Memory Works
- User sends message
- Message appended to history list
- Full history sent to Gemini
- Gemini reads entire conversation
- Context-aware response generated
- Response appended to history
- Cycle continues with growing context!

Tech Stack
Google Gemini 2.5
Gradio
python-dotenv
Hugging Face Spaces

Author
Hamza Roohani

Hugging Face: HamzaRoohani

License
This project is licensed under the MIT License.