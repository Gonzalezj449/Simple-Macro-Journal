# Page2.py
import tkinter as tk
import json

class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        username_label = tk.Label(self, text="Username:", font=("Arial", 16))
        username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self, font=("Arial", 16))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(self, text="Password:", font=("Arial", 16))
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        create_account_button = tk.Button(self, text="Create Account", command=self.create_account, font=("Arial", 16))
        create_account_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.account_message_label = tk.Label(self, text="", font=("Arial", 16))
        self.account_message_label.grid(row=3, column=0, columnspan=2)

        # Button to return to LoginPage, initially not visible
        self.return_login_button = tk.Button(self, text="Return to Login", command=lambda: self.controller.show_page("LoginPage"), font=("Arial", 16))
        self.return_login_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.return_login_button.grid_remove()  # Hide the button initially

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            try:
                with open("accounts.json", "r") as f:
                    accounts = json.load(f)
            except FileNotFoundError:
                accounts = {}
            if username in accounts:
                self.account_message_label.config(text="Username already exists.")
            else:
                accounts[username] = password
                with open("accounts.json", "w") as f:
                    json.dump(accounts, f)
                self.account_message_label.config(text="Account created successfully.")
                self.return_login_button.grid()  # Show the button upon successful account creation
        else:
            self.account_message_label.config(text="Please enter both username and password.")

        
