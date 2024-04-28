import tkinter as tk
import json

class ChatWithStaff(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.messages = []  # List to store messages
        self.create_widgets()
        self.load_messages()

    def create_widgets(self):
        # Label for the title
        title_label = tk.Label(self, text="User Dashboard: Chatting With Staff...", font=("Arial", 20))
        title_label.pack(pady=20)

        # Chat display area for staff's messages (read-only)
        self.staff_chat_display = tk.Text(self, width=50, height=20)
        self.staff_chat_display.pack(pady=10)
        self.staff_chat_display.config(state=tk.DISABLED)  # Make the text area read-only

        # Label to display initial message
        initial_message_label = tk.Label(self, text="To request food, please state the food item you would like to add.", font=("Arial", 12))
        initial_message_label.pack(pady=5)

        # Entry field for typing messages to the staff
        self.staff_message_entry = tk.Entry(self, width=50)
        self.staff_message_entry.pack(pady=5)

        # Button to send messages to the staff
        send_button = tk.Button(self, text="Send", command=self.send_staff_message)
        send_button.pack(pady=5)

        # Button to go back to the previous page
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(pady=10)

    def load_messages(self):
        try:
            with open("inbox.json", "r") as f:
                self.messages = json.load(f)
            self.display_messages()
        except FileNotFoundError:
            self.messages = []

    def save_messages(self):
        with open("inbox.json", "w") as f:
            json.dump(self.messages, f)

    def add_message(self, sender, message):
        self.messages.append({"sender": sender, "message": message})
        self.save_messages()

    def display_messages(self):
        for message in self.messages:
            sender = message["sender"]
            msg = message["message"]
            self.staff_chat_display.config(state=tk.NORMAL)  # Enable editing temporarily
            self.staff_chat_display.insert(tk.END, f"{sender}: {msg}\n")
            self.staff_chat_display.config(state=tk.DISABLED)  # Make the text area read-only again

    def send_staff_message(self):
        # Get the message from the entry field
        message = self.staff_message_entry.get()
        if message:
            # Save the message
            self.add_message("user", message)
            # Display the message in the chat display area
            self.staff_chat_display.config(state=tk.NORMAL)  # Enable editing temporarily
            self.staff_chat_display.insert(tk.END, f"You: {message}\n")
            self.staff_chat_display.config(state=tk.DISABLED)  # Make the text area read-only again
            # Clear the entry field
            self.staff_message_entry.delete(0, tk.END)



    def go_back(self):
        # Navigate back to the previous page and save the messages
        self.save_messages()
        self.parent.show_page("CaloriePage")
