# Simple Chatbot

def greet():
    print("Hi there! I'm your chatbot.")
    print("What's your name?")

def chat():
    greet()
    name = input("> ")
    print(f"Nice to meet you, {name}!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

def get_response(input_text):
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm good, thank you!",
        "bye": "Goodbye!",
        # Add more responses here
    }

    if input_text.lower() in responses:
        return responses[input_text.lower()]
    else:
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    chat()
