def chatbot_response(user_input):
    
    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    
    elif user_input == "what is your name":
        return "I am a simple Python chatbot."
    
    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that."


print("🤖 Welcome to Basic Chatbot!")
print("Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ").lower()
    
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    if user_input == "bye":
        break
