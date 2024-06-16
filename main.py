import re
import random

# Define a dictionary of response0 
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, how about you?", "Doing well, thanks!", "I'm fine, thank you!"],
    "your name": ["I'm a chatbot created by a Python script.", "I don't have a name, but you can call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

# Define a function to find the appropriate response
def match_response(user_input):
    for pattern, responses_list in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses_list)
    return "I don't understand that. Can you ask something else?"

# Main function to run the chatbot
def chatbot():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        response = match_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot()
