# Rule-Based Chatbot - CODSOFT Internship Task 1

def chatbot():
    print("Welcome to the Rule-Based Chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello. How can I assist you today?")

        elif "how are you" in user_input:
            print("Bot: I am functioning properly. Thank you for asking.")

        elif "your name" in user_input:
            print("Bot: I am a rule-based chatbot created for the CODSOFT AI Internship.")

        elif "help" in user_input:
            print("Bot: You can greet me, ask my name, or ask how I am.")

        elif "what can you do" in user_input:
            print("Bot: I can respond to basic predefined questions using rule-based logic.")

        elif user_input == "bye":
            print("Bot: Goodbye. Have a nice day.")
            break

        else:
            print("Bot: I do not understand that query. Please try something else.")

if __name__ == "__main__":
    chatbot()