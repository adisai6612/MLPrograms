def simple_chatbot():
    print("Hi there! I'm a simple chatbot.")
    print("You can type 'exit' to leave the conversation.")

    while True:
        user_input = input("You: ")
        user_input = user_input.lower()

        if user_input in ['hello', 'hi', 'hey']:
            print("Bot: Hi there!")
        elif user_input in ['how are you?', 'how are you doing?']:
            print("Bot: I'm just a bot, but I'm here to help!")
        elif user_input in ['exit', 'bye', 'goodbye']:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    simple_chatbot()

