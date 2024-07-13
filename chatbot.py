# Simple Chatbot using NLP

import random

greetings = ["Hello!", "Hi there!", "Hey!", "Hi!", "Greetings!"]
responses = ["I'm a chatbot.", "How can I assist you?", "I'm here to help.", "What can I do for you?"]

def chatbot_response(user_input):
    if user_input.lower() in ["hello", "hi", "hey"]:
        return random.choice(greetings)
    else:
        return random.choice(responses)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chatbot_response(user_input))
