import nltk
from nltk.chat.util import Chat, reflections

# Define conversation pairs
pairs = [
    ["hello|hi|hey", ["Hi there! I am your friendly chatbot. You can ask me some common things. How can I help you?"]],
    ["how are you", ["I'm doing great, thanks for asking!", "I'm good! How about you?"]],
    ["yes i am fine", ["Happy to hear this! How can I help you?"]],
    ["what can you do", [
        "I can chat with you, answer questions, and keep you entertained!",
        "I'm here to assist you with anything you need."
    ]],
    ["who created you", [
        "I was created by an amazing developer—you!",
        "I'm the result of your awesome coding skills!"
    ]],
    ["tell me a joke", [
        "Why did the computer catch a cold? Because it left its Windows open!",
        "I told my Wi-Fi it was feeling weak—it said it needed a stronger connection!"
    ]],
    ["bye", [
        "Goodbye! Have a great day!",
        "See you soon!",
        "Take care!"
    ]],
    ["tell me something interesting", [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are still good to eat!"
    ]],
    ["do you like music", [
        "I enjoy all kinds of music! What’s your favorite genre?"
    ]],
    ["recommend a movie", [
        "How about ‘Inception’? It’s a mind-bending masterpiece!",
        "I’d suggest watching ‘Interstellar’ if you like sci-fi!"
    ]],
    ["what is the capital of India", [
        "The capital of India is New Delhi."
    ]],
    ["how old are you", [
        "I don’t age like humans, but I’m as old as the code that created me!"
    ]],
    ["can you help me", [
        "Of course! What do you need help with?"
    ]],
        ["do you have feelings", [
        "I don’t have feelings like humans, but I do enjoy chatting with you!"
    ]],
    ["what is life", [
        "Life is a beautiful journey of learning, growing, and experiencing new things!"
    ]],
    ["who is the prime minister of India", [
        "The current Prime Minister of India is Narendra Modi."
    ]],
    ["what is your favorite food", [
        "I don’t eat, but I’ve heard pizza is quite popular!"
    ]],
    ["what is the largest ocean?", ["The largest ocean is the Pacific Ocean."]],
    ["How many days in a week?", ["There are seven days in a week."]],
    ]
# Create chatbot instance
chatbot = Chat(pairs, reflections)

print("🤖 Hello! I'm your chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower().strip()
    if user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    response = chatbot.respond(user_input)
    if response:
        print("Bot:", response)
    else:
        print("Bot: I didn't understand that.")
