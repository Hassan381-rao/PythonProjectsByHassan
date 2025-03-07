
import tkinter as tk
from tkinter import scrolledtext
import openai

class ChatApplication:
    def __init__(self, root, api_key):
        self.root = root
        self.root.title("Simple Chat Application")
        
        
        self.api_key = api_key
        openai.api_key = self.api_key
        
        self.conversation_history = []

        self.chat_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_window.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
        
        self.message_entry = tk.Entry(self.root, font=("Arial", 12))
        self.message_entry.pack(padx=20, pady=5, fill=tk.X)
        
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=20, pady=5)
    
    def send_message(self, event=None):
        message = self.message_entry.get()
        if message.strip():
            self.display_message("You", message)
            self.message_entry.delete(0, tk.END)
            self.conversation_history.append({"role": "user", "content": message})
            self.bot_reply()
    
    def display_message(self, sender, message):
        self.chat_window.configure(state='normal')
        self.chat_window.insert(tk.END, f"{sender}: {message}\n")
        self.chat_window.configure(state='disabled')
        self.chat_window.yview(tk.END)
    
    def bot_reply(self):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=self.conversation_history + [{"role": "system", "content": "You are a helpful assistant."}]
            )
            bot_message = response['choices'][0]['message']['content'].strip()
            self.display_message("Bot", bot_message)
            self.conversation_history.append({"role": "assistant", "content": bot_message})
        except Exception as e:
            self.display_message("Bot", "Sorry, I couldn't process that. Please try again.")
            print(f"Error: {e}")

if __name__ == "__main__":
    api_key = 'your_openai_api_key_here'
    root = tk.Tk()
    app = ChatApplication(root, api_key)
    root.geometry("400x300")
    root.mainloop()
