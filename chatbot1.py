import spacy
import random

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    # Process user input using spaCy
    doc = nlp(user_input)

    # Define patterns and corresponding responses
    patterns = [
        (["hello", "hi", "hey"], ["Hi there!", "Hello!", "Hey!"]),
        (["how are you", "how do you do"], ["I'm just a bot, but I'm doing well. How can I assist you?"]),
        (["your name", "who are you", "what's your name"], ["I'm a chatbot. You can call me ChatGPT!"]),
        (["bye", "goodbye", "see you later"], ["Goodbye!", "Farewell!", "See you later!"]),
        (["thanks", "thank you", "thanks a lot"], ["You're welcome!", "No problem!", "Happy to help!"]),
        (["joke", "tell me a joke"], ["Why did the computer go to therapy? It had too many bytes of emotional baggage!"]),
        # Add more patterns and responses here
    ]

    # Check if the user's input matches any pattern
    for pattern, response_options in patterns:
        if any(token.text.lower() in pattern for token in doc):
            return random.choice(response_options)

    # If no pattern matches, provide a default response
    return "I'm not sure how to respond to that. Can we talk about something else?"

def chatbot():
    print("Chat: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chat: Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        print("Chat:", response)

if __name__ == "__main__":
    chatbot()
