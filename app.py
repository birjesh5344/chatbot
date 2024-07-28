import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a bot created by you. You can call me ChatBot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "It's OK, never mind.",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?",]
    ],
]

# Create the chatbot
def chatbot():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
if __name__ == "__main__":
    chatbot()
