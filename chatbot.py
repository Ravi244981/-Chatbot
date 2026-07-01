def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day!")
            break

        elif "hello" in user or "hi" in user:
            print("🤖 ChatBot: Hello! How can I help you?")

        elif "how are you" in user:
            print("🤖 ChatBot: I'm doing great! Thanks for asking.")

        elif "your name" in user:
            print("🤖 ChatBot: I'm a simple Python chatbot.")

        elif "time" in user:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 ChatBot: The current time is {current_time}")

        elif "date" in user:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"🤖 ChatBot: Today's date is {current_date}")

        elif "help" in user:
            print("🤖 ChatBot: You can ask me about the time, date, or just chat!")

        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()