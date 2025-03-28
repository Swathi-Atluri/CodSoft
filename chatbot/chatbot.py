import re
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r"\byeee|goodbye\b", user_input):
        return "Goodbye! Have a great day!"
    
    # Basic Info
    elif "your name" in user_input:
        return "I'm chatty, a rule based chatbot!"
    elif "who created you" in user_input:
        return "I was created by a AI developer!"
    
    # Date & Time
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    
    # Weather
    elif "weather" in user_input:
        return "I can't check the weather, but you can visit weather.com for updates."
    
    # Math calculations
    elif re.search(r"\b\d+\s*[+\-*/]\s*\d+\b", user_input):
        try:
            return f"The answer is {eval(user_input)}"
        except:
            return "Sorry, I couldn't process that calculation."
    
    # General Knowledge
    elif "president of usa" in user_input:
        return "The current president of the USA is Joe Biden."
    elif "who discovered gravity" in user_input:
        return "Sir Isaac Newton discovered gravity."
    
    # Science & Space
    elif "black hole" in user_input:
        return "A black hole is a region in space where gravity is so strong that nothing can escape from it."
    
    # Technology
    elif "what is ai" in user_input:
        return "AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines."
    elif "machine learning" in user_input:
        return "Machine learning is a branch of AI that allows computers to learn from data."
    
    # Health & Fitness
    elif "lose weight" in user_input:
        return "A healthy diet and regular exercise are key to weight loss."
    
    # Entertainment
    elif "latest movies" in user_input:
        return "Check out IMDb for the latest movie updates!"
    
    # Sports
    elif "fifa world cup winner" in user_input:
        return "Argentina won the FIFA World Cup 2022."
    
    # Fun & Jokes
    elif "tell me a joke" in user_input:
        return "Why don’t skeletons fight each other? Because they don’t have the guts!"
    elif "give me a riddle" in user_input:
        return "I speak without a mouth and hear without ears. What am I? (Answer: An Echo)"
    
    # Emergency Help
    elif "earthquake" in user_input:
        return "If you are in an earthquake, drop, cover, and hold on!"
    
    # Default Response
    else:
        return "I'm not sure about that. Can you ask something else?"

# Run chatbot loop
print("Chatbot: Hello! Type 'exit' to end the chat.")
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_query)
    print(f"Chatbot: {response}")
