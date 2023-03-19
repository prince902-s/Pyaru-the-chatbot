import random

# Define some responses
responses = {
    "hi": "Hello!",
    "how are you?": "I'm doing well, thank you!",
    "what's your name?": "My name is Pyaru!",
"do you know my name": "nope! would you mind telling me your name😁",
"my name is Prince": "oh! hi prince",
"I'm prince": "hi prince",

"default": "I'm sorry, I didn't understand what you said. Can you please try again?"
}

# Define the chat function
def chat():
    while True:
        # Get user input
        user_input = input("You: ")

        # Convert input to lowercase
        user_input = user_input.lower()

        # Check if user input matches a response
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot:", responses["default"])

# Start the chat
chat()
