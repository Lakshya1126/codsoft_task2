def chatbot():
    print("Hello! I am a simple chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking!")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you!")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
            
chatbot()
