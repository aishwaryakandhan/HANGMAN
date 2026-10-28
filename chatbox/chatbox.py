print("================================")
print("       HERBAL CHATBOT")
print("================================")
print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine! Thank you.")

    elif user_input == "what is your name":
        print("Bot: I am a Python chatbot.")

    elif user_input == "help":
        print("Bot: You can say hello, ask my name, or ask how I am.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that message.")
