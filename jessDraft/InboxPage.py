import tkinter as tk
import json

class InboxPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.messages = []  # List to store messages
        self.create_widgets()
        self.load_messages()

    def create_widgets(self):
        # Label for the title
        title_label = tk.Label(self, text="Inbox", font=("Arial", 20))
        title_label.pack(pady=20)

        # Text area to display messages
        self.message_display = tk.Text(self, width=50, height=20)
        self.message_display.pack(pady=10)

        # Button to go back to the previous page
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(pady=10)

    def load_messages(self):
        try:
            with open("messages.json", "r") as f:
                self.messages = json.load(f)
                self.display_messages()
        except FileNotFoundError:
            self.messages = []

    def save_messages(self):
        with open("messages.json", "w") as f:
            json.dump(self.messages, f)

    def add_message(self, message):
        self.messages.append(message)
        self.save_messages()
        self.display_messages()

    def display_messages(self):
        self.message_display.config(state=tk.NORMAL)  # Enable editing temporarily
        self.message_display.delete('1.0', tk.END)  # Clear existing messages
        for msg in self.messages:
            self.message_display.insert(tk.END, f"{msg}\n")
        self.message_display.config(state=tk.DISABLED)  # Make the text area read-only again

    def go_back(self):
        # Navigate back to the previous page
        self.parent.show_page("StaffDashB")
