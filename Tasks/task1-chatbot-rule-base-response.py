# CHATBOT WITH RULE-BASED RESPONSES
# Build a simple chatbot that responds to user inputs based on predefined rules. 
# Use if-else statements or pattern matching techniques to identify user queries 
# and provide appropriate responses. This will give you a basic understanding of 
# natural language processing and conversation flow.

# predefined rules
chatbot_reponses = {
    "hello": "hello! How i can help you!",
    "thanks": "your welcome!",
    "thank you": "your welcome!",
    "what is your name?": "i am chatbot! you can call me Atique Chatbot",
    "hi": "hi! How i can help you!",
    "ok": "thank you",
    "your welcome!": "my pleaseure!",
    "your welcome": "my pleaseure!",
}

while True:
    user_input = input("User: " ).lower()
    if user_input == "quit":
        print("chatbot: Goodbye!")
        break
    if user_input in chatbot_reponses:
        print("chatbot: ", chatbot_reponses[user_input])
    else:
        print("chatbot: I'm not sure how to respond to that!")
