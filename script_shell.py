import os
import openai

class Chatbot:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.chat_history = []

    def append_to_chat_history(self, message):
        self.chat_history.append(message)

    def create_chat_response(self, message):
        self.append_to_chat_history(message)

        messages = [
            {"role": "system", "content": "You are the most helpful assistant."},
            {"role": "user", "content": message},
            {"role": "assistant", "content": message}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )

        bot_response = response.choices[0].message['content'].strip()
        self.append_to_chat_history(bot_response)
        return bot_response

    def start_chatting(self):
        print("Chatbot: Hello! I'm here to assist you. Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break
            bot_response = self.create_chat_response(user_input)
            print("Chatbot:", bot_response)

chatbot = Chatbot()
chatbot.start_chatting()
