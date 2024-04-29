import tkinter as tk
import json

class ChatWithUserForDoc(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.messages = []  # List to store messages
        self.create_widgets()
        self.load_messages()

    def create_widgets(self):
        # Label for the title
        title_label = tk.Label(self, text="Doctor Dashboard: Chatting With User...", font=("Arial", 20))
        title_label.pack(pady=20)

        # Chat display area for user's messages (read-only)
        self.user_chat_display = tk.Text(self, width=50, height=20)
        self.user_chat_display.pack(pady=10)
        self.user_chat_display.config(state=tk.DISABLED)  # Make the text area read-only

        # Entry field for typing messages to the user
        self.user_message_entry = tk.Entry(self, width=50)
        self.user_message_entry.pack(pady=5)

        # Button to send messages to the user
        send_button = tk.Button(self, text="Send", command=self.send_user_message)
        send_button.pack(pady=5)

        # Button to go back to the previous page
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(pady=10)

    def load_messages(self):
        try:
            with open("inboxDoctor.json", "r") as f:
                self.messages = json.load(f)
            self.display_messages()
        except FileNotFoundError:
            self.messages = []

    def save_messages(self):
        with open("inboxDoctor.json", "w") as f:
            json.dump(self.messages, f)

    def add_message(self, sender, message):
        self.messages.append({"sender": sender, "message": message})
        self.save_messages()

    def display_messages(self):
        for message in self.messages:
            sender = message["sender"]
            msg = message["message"]
            self.user_chat_display.config(state=tk.NORMAL)  # Enable editing temporarily
            self.user_chat_display.insert(tk.END, f"{sender}: {msg}\n")
            self.user_chat_display.config(state=tk.DISABLED)  # Make the text area read-only again

    def send_user_message(self):
        # Get the message from the entry field
        message = self.user_message_entry.get()
        if message:
            # Save the message
            self.add_message("Doctor", message)
            # Display the message in the chat display area
            self.user_chat_display.config(state=tk.NORMAL)  # Enable editing temporarily
            self.user_chat_display.insert(tk.END, f"You: {message}\n")
            self.user_chat_display.config(state=tk.DISABLED)  # Make the text area read-only again
            # Clear the entry field
            self.user_message_entry.delete(0, tk.END)

    def go_back(self):
        # Navigate back to the previous page and save the messages
        self.save_messages()
        self.parent.show_page("DocDashB")
