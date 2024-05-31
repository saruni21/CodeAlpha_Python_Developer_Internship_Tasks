import spacy
from random import choice

# Load the small English NLP model
nlp = spacy.load("en_core_web_sm")

class Chatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you today?"],
            "goodbye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
            "weather": ["I'm not sure about the weather. Maybe check a weather app?", "I can't provide weather updates at the moment."],
            "default": ["I'm not sure how to respond to that.", "Can you please rephrase?", "I'm here to help. Ask me anything."]
        }

    def get_response(self, user_input):
        doc = nlp(user_input)
        if any(token.lower_ in ["hello", "hi", "hey", "greetings"] for token in doc):
            return choice(self.responses["greeting"])
        elif any(token.lower_ in ["bye", "goodbye", "see you", "later"] for token in doc):
            return choice(self.responses["goodbye"])
        elif "weather" in user_input.lower():
            return choice(self.responses["weather"])
        else:
            return choice(self.responses["default"])

# Initialize the chatbot
chatbot = Chatbot()

# Function to chat with the bot
def chat_with_bot():
    print("Chatbot: Hello! I'm here to chat with you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
chat_with_bot()
